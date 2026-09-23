from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Livro
from .forms import LivroForm

# Create your tests here.
class LivroTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.ano_atual = timezone.localdate().year

        self.livro1 = Livro.objects.create(
            titulo='Dom Casmurro',
            autor='Machado de Assis',
            ano=1899,
            disponivel=True
        )
        self.livro2 = Livro.objects.create(
            titulo='Memórias Póstumas de Brás Cubas',
            autor='Machado de Assis',
            ano=1881,
            disponivel=False
        )
        self.livro3 = Livro.objects.create(
            titulo='O Hobbit',
            autor='J. R. R. Tolkien',
            ano=1937,
            disponivel=True
        )

    # =========================================================================
    # Feature 2: Validação de ano de publicação no LivroForm
    # =========================================================================
    def test_ano_futuro_rejeitado_no_form(self):
        """Testa se o formulário fica inválido com ano futuro."""
        form = LivroForm(data={
            'titulo': 'Livro do Futuro',
            'autor': 'Viajante',
            'ano': self.ano_atual + 1,
            'disponivel': True
        })
        self.assertFalse(form.is_valid())
        self.assertIn('ano', form.errors)

    def test_ano_futuro_rejeitado_na_view_e_nao_salva_no_banco(self):
        """Testa se envio de ano futuro não salva o livro e exibe o erro na página."""
        qtd_antes = Livro.objects.count()
        response = self.client.post(reverse('cadastrar'), {
            'titulo': 'Livro do Futuro',
            'autor': 'Viajante',
            'ano': self.ano_atual + 5,
            'disponivel': True
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Livro.objects.count(), qtd_antes)
        self.assertContains(
            response,
            f'O ano de publicação não pode ser no futuro. O ano máximo permitido é {self.ano_atual}.'
        )

    def test_ano_atual_aceito(self):
        """Testa se o ano atual é considerado válido."""
        form = LivroForm(data={
            'titulo': 'Livro Contemporâneo',
            'autor': 'Autor Atual',
            'ano': self.ano_atual,
            'disponivel': True
        })
        self.assertTrue(form.is_valid())

    def test_ano_passado_aceito(self):
        """Testa se um ano passado é considerado válido."""
        form = LivroForm(data={
            'titulo': 'Livro Histórico',
            'autor': 'Autor Antigo',
            'ano': 1900,
            'disponivel': True
        })
        self.assertTrue(form.is_valid())

    # =========================================================================
    # Feature 1: Busca e Filtro na listagem
    # =========================================================================
    def test_sem_filtro_lista_tudo_ordenado_por_titulo(self):
        """Testa se a listagem sem parâmetros lista todos os livros ordenados por título."""
        response = self.client.get(reverse('lista'))
        self.assertEqual(response.status_code, 200)
        livros_retornados = list(response.context['livros'])
        self.assertEqual(len(livros_retornados), 3)
        self.assertEqual(livros_retornados[0], self.livro1)
        self.assertEqual(livros_retornados[1], self.livro2)
        self.assertEqual(livros_retornados[2], self.livro3)

    def test_busca_por_titulo_ignora_maiusculas(self):
        """Testa se a busca por título não diferencia maiúsculas de minúsculas (icontains)."""
        response = self.client.get(reverse('lista'), {'q': 'dom'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dom Casmurro')
        self.assertNotContains(response, 'O Hobbit')

    def test_busca_por_autor(self):
        """Testa se a busca encontra livros pelo nome do autor."""
        response = self.client.get(reverse('lista'), {'q': 'tolkien'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'O Hobbit')
        self.assertNotContains(response, 'Dom Casmurro')

    def test_filtro_disponivel(self):
        """Testa o filtro por status 'disponivel'."""
        response = self.client.get(reverse('lista'), {'status': 'disponivel'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dom Casmurro')
        self.assertContains(response, 'O Hobbit')
        self.assertNotContains(response, 'Memórias Póstumas')

    def test_filtro_emprestado(self):
        """Testa o filtro por status 'emprestado'."""
        response = self.client.get(reverse('lista'), {'status': 'emprestado'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Memórias Póstumas')
        self.assertNotContains(response, 'Dom Casmurro')
        self.assertNotContains(response, 'O Hobbit')

    def test_busca_e_filtro_juntos(self):
        """Testa a combinação de busca por texto com filtro de status na mesma consulta."""
        response = self.client.get(reverse('lista'), {'q': 'machado', 'status': 'disponivel'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dom Casmurro')
        self.assertNotContains(response, 'Memórias Póstumas')
        self.assertNotContains(response, 'O Hobbit')

    def test_mensagem_quando_nenhum_livro_encontrado(self):
        """Testa mensagem exibida quando nenhum livro atende aos filtros aplicados."""
        response = self.client.get(reverse('lista'), {'q': 'inexistente_123'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nenhum livro encontrado para os filtros aplicados.')

    def test_campo_q_continua_preenchido(self):
        """Testa se o valor pesquisado é mantido no campo de texto da tela."""
        termo = 'Machado'
        response = self.client.get(reverse('lista'), {'q': termo})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'value="{termo}"')

    # =========================================================================
    # CRUD: Editar e Excluir
    # =========================================================================
    def test_editar_livro_get(self):
        """Testa se o GET da tela de edição exibe o formulário preenchido com dados do livro."""
        response = self.client.get(reverse('editar', kwargs={'pk': self.livro1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dom Casmurro')
        self.assertContains(response, 'Editar Livro')

    def test_editar_livro_post(self):
        """Testa se o POST na edição atualiza o livro no banco e redireciona para 'lista'."""
        response = self.client.post(
            reverse('editar', kwargs={'pk': self.livro1.pk}),
            {
                'titulo': 'Dom Casmurro - Edição Especial',
                'autor': 'Machado de Assis',
                'ano': 1900,
                'disponivel': False
            }
        )
        self.assertRedirects(response, reverse('lista'))
        self.livro1.refresh_from_db()
        self.assertEqual(self.livro1.titulo, 'Dom Casmurro - Edição Especial')
        self.assertEqual(self.livro1.ano, 1900)
        self.assertFalse(self.livro1.disponivel)

    def test_excluir_livro_get_mostra_confirmacao(self):
        """Testa se o GET da exclusão apenas mostra a tela de confirmação sem apagar o livro."""
        response = self.client.get(reverse('excluir', kwargs={'pk': self.livro1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Confirmar Exclusão')
        self.assertContains(response, 'Dom Casmurro')
        self.assertTrue(Livro.objects.filter(pk=self.livro1.pk).exists())

    def test_excluir_livro_post_deleta_e_redireciona(self):
        """Testa se o POST da exclusão realmente remove o livro do banco e redireciona."""
        pk = self.livro1.pk
        response = self.client.post(reverse('excluir', kwargs={'pk': pk}))
        self.assertRedirects(response, reverse('lista'))
        self.assertFalse(Livro.objects.filter(pk=pk).exists())

