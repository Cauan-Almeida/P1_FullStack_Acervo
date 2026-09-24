# 📚 Sistema de Biblioteca / Acervo — Entrega P1

**Universidade de Vassouras**  
**Curso de Graduação em Engenharia de Software**  
**Disciplina:** Laboratório de Programação Full Stack  
**Professor:** Prof. Márcio Garrido  
**Aluno:** Cauan Ferreira de Almeida  
**Matrícula:** 202323031  
**Repositório GitHub:** [https://github.com/Cauan-Almeida/P1_FullStack_Acervo.git](https://github.com/Cauan-Almeida/P1_FullStack_Acervo.git)

---

## 📝 Relatório da Entrega P1

### Justificativa das Decisões de Projeto

* **Feature 1 — Busca e Filtro na Listagem (com Desafio Extra `Q()`):**  
  Para a Feature 1, foi implementada a busca textual combinada nos campos `titulo` ou `autor` através de `(Q(titulo__icontains=q) | Q(autor__icontains=q))` e o filtro por situação através do campo booleano `disponivel` (`status='disponivel'` para `True` e `status='emprestado'` para `False`). Ambos foram encadeados na **mesma consulta** com o operador `&` (`filtro &= ...`) e os resultados ordenados alfabeticamente (`.order_by('titulo')`).  
  *Por que escolhemos esses campos:* Em um sistema real de biblioteca, os leitores pesquisam tanto pelo nome do livro quanto pelo nome do autor e necessitam verificar de imediato se a obra está disponível para empréstimo no acervo físico. Se essa funcionalidade não existisse, o leitor precisaria inspecionar visualmente todos os registros de uma listagem extensa, inviabilizando a usabilidade do sistema à medida que o catálogo crescesse.

* **Feature 2 — Validação Customizada no Formulário (`clean_ano`):**  
  Para a Feature 2, foi sobrescrito o método `clean_ano()` na classe `LivroForm` (`ModelForm`), utilizando `timezone.localdate().year` para comparar o valor informado com o ano atual do servidor. Caso o ano seja maior que o ano corrente, uma exceção `forms.ValidationError` é lançada com mensagem clara indicando o ano máximo permitido.  
  *Por que escolhemos essa regra:* No domínio de uma biblioteca, um livro físico não pode possuir data de publicação em um ano futuro. Se essa regra de validação não existisse, o sistema permitiria a inserção de registros anacrônicos ou fictícios, violando a integridade e a credibilidade dos dados bibliográficos armazenados.

---

## ⚙️ Funcionalidades Implementadas (CRUD Completo + Features)

1. **Página Inicial (Home):**
   * Painel de boas-vindas com resumo quantitativo do acervo: total de livros, quantidade de disponíveis e quantidade de emprestados.
   * Botões de navegação rápida para o acervo e para o formulário de cadastro.
2. **Listagem e Busca (`/livros/`):**
   * Exibição de título, autor, ano de publicação e situação textual (*Disponível* ou *Emprestado*).
   * Formulário `GET` integrado para busca textual (título OU autor) e filtro por status (Todos / Disponíveis / Emprestados).
   * Preservação do termo digitado no input (`value="{{ request.GET.q }}"`) e da opção selecionada no `<select>`.
   * Feedback claro quando nenhum registro é encontrado via bloco `{% empty %}`: *"Nenhum livro encontrado para os filtros aplicados."*.
   * Link para limpar os filtros aplicados e reexibir a lista completa ordenada.
3. **Cadastro (`/cadastrar/`):**
   * Formulário dinâmico utilizando `ModelForm` com proteção `{% csrf_token %}`.
   * Validação em tempo de submissão impedindo o cadastro de anos futuros via `clean_ano()`.
4. **Edição (`/livros/<id>/editar/`):**
   * Reaproveitamento do template `form.html` com título dinâmico `{{ titulo }}` (*Editar Livro*).
   * Recuperação segura do registro via `get_object_or_404(Livro, pk=pk)` e salvamento com `instance=livro`.
5. **Exclusão (`/livros/<id>/excluir/`):**
   * Tela de confirmação intermediária (`confirmar_exclusao.html`) no método `GET`, prevenindo exclusões acidentais.
   * Exclusão definitiva do banco executada exclusivamente via requisição `POST` com redirecionamento para a lista.
   * Botão/link de cancelamento que retorna com segurança para a listagem sem alterar o banco.

---

## 🚀 Como Executar o Projeto

### 1. Ativar o Ambiente Virtual
* **No macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```
* **No Windows:**
  ```bash
  venv\Scripts\activate
  ```

### 2. Executar as Migrações
```bash
python manage.py migrate
```

### 3. Iniciar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```

Acesse no navegador:
* 🏠 **Página Inicial:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* 📚 **Acervo de Livros:** [http://127.0.0.1:8000/livros/](http://127.0.0.1:8000/livros/)
* ➕ **Cadastrar Livro:** [http://127.0.0.1:8000/cadastrar/](http://127.0.0.1:8000/cadastrar/)
* 🔒 **Painel Administrativo:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
