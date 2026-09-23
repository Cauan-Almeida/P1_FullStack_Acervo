# 📚 Sistema de Biblioteca Central & Acervo (Django)

Este projeto foi desenvolvido como parte das práticas de **Laboratório de Programação Full Stack (Aulas 4 e 5)** e serve de base para o projeto da **P1**.

O sistema gerencia um acervo bibliográfico com cadastro e listagem de livros, renderização de templates via Django Template Language (DTL), estilização com arquivos estáticos (CSS), persistência em banco de dados e painel administrativo integrado.

---

## 📁 Estrutura do Projeto

```text
AULA_4_e_5_na_mão/
├── biblioteca/             # Configurações do projeto Django
│   ├── settings.py         # Configuração de apps, banco de dados, templates e static
│   ├── urls.py             # Roteador principal do projeto
│   ├── asgi.py
│   └── wsgi.py
├── acervo/                 # App principal do sistema de biblioteca
│   ├── migrations/         # Histórico de migrações do banco
│   ├── templates/          # Templates HTML
│   │   ├── base.html       # Template base com header, navegação e footer
│   │   └── acervo/
│   │       ├── lista.html  # Tela de listagem de livros
│   │       └── form.html   # Tela de cadastro de novos livros
│   ├── static/             # Arquivos estáticos
│   │   └── acervo/
│   │       └── estilo.css  # Folha de estilos CSS da aplicação
│   ├── admin.py            # Registro dos modelos no Django Admin
│   ├── forms.py            # Formulários (ModelForm)
│   ├── models.py           # Modelos de banco de dados (Livro)
│   ├── urls.py             # Rotas específicas do app acervo
│   └── views.py            # Regras de negócio e renderização de telas
├── db.sqlite3              # Banco de dados local (SQLite)
├── manage.py               # Utilitário de linha de comando do Django
├── .env                    # Variáveis de ambiente (ignorado no Git)
├── .gitignore              # Regras de exclusão de arquivos no Git
├── objetivo.md             # Roteiro original das aulas 4 e 5
└── README.md               # Este guia completo
```

---

## 🚀 Como Rodar o Projeto Passo a Passo

### 1. Clonar ou Acessar a Pasta do Projeto
Abra o seu terminal e navegue até a pasta do projeto:
```bash
cd "caminho/para/AULA_4_e_5_na_mão"
```

---

### 2. Ativar o Ambiente Virtual (`venv`)

> [!NOTE]
> O ambiente virtual isola os pacotes e versões do Python instalados no projeto.

- **No macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

- **No Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```
  *(Se der erro de permissão no PowerShell, execute antes: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

- **No Windows (Prompt de Comando - CMD):**
  ```cmd
  venv\Scripts\activate.bat
  ```

*(Quando ativado, o prefixo `(venv)` aparecerá no início da linha do terminal).*

Se precisar recriar a virtualenv do zero algum dia:
```bash
# macOS / Linux
python3 -m venv venv

# Windows
python -m venv venv
```

---

### 3. Instalar as Dependências

Com a `venv` ativada, execute:
```bash
pip install django python-dotenv psycopg2-binary
```

---

### 4. Configuração do Banco de Dados

O projeto está configurado no arquivo `biblioteca/settings.py` para operar de duas maneiras:

1. **SQLite (Automático / Padrão sem configuração extra):**
   - Ideal para testes rápidos ou se você não tiver o PostgreSQL configurado na máquina.
   - Para forçar o uso do SQLite, basta colocar no seu arquivo `.env`:
     ```env
     USE_SQLITE=True
     ```
2. **PostgreSQL (Com arquivo `.env`):**
   - Caso você tenha um banco PostgreSQL rodando localmente, crie ou edite o `.env`:
     ```env
     DB_NAME=meu_banco
     DB_USER=postgres
     DB_PASSWORD=postgres
     DB_HOST=localhost
     DB_PORT=5432
     ```

---

### 5. Executar as Migrações do Banco de Dados

Sempre que criar ou alterar modelos, execute:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Criar um Superusuário (Administrador)

Para acessar o painel administrativo do Django e cadastrar dados diretamente:
```bash
python manage.py createsuperuser
```
*(Siga as instruções informando nome de usuário, e-mail e senha).*

---

### 7. Iniciar o Servidor Local

```bash
python manage.py runserver
```

Acesse no seu navegador:
* 🌐 **Página Inicial:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) *(Mensagem de boas-vindas do acervo)*
* 📚 **Listagem de Livros:** [http://127.0.0.1:8000/livros/](http://127.0.0.1:8000/livros/)
* ➕ **Cadastrar Livro:** [http://127.0.0.1:8000/cadastrar/](http://127.0.0.1:8000/cadastrar/)
* 🔒 **Painel Administrativo:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🐙 Como Subir o Projeto no GitHub Passo a Passo

Siga este roteiro para subir o seu projeto no GitHub pela primeira vez de forma segura:

### Passo 1: Inicializar o Repositório Local
Na raiz do projeto (onde está o `manage.py`), digite:
```bash
git init
```

### Passo 2: Conferir o `.gitignore`
Certifique-se de que a pasta `venv/`, o arquivo `.env` e os caches `__pycache__` estão sendo ignorados:
```bash
git status
```
*(Você **NÃO** deve ver a pasta `venv/` nem o arquivo `.env` na lista de arquivos para envio).*

### Passo 3: Adicionar os Arquivos
Adicione os arquivos do projeto ao estágio de preparação:
```bash
git add .
```

### Passo 4: Fazer o Primeiro Commit
```bash
git commit -m "feat: projeto biblioteca aulas 4 e 5 concluidas com base para P1"
```

### Passo 5: Renomear a Branch Principal para `main`
```bash
git branch -M main
```

### Passo 6: Criar o Repositório no GitHub
1. Acesse [github.com](https://github.com) e entre na sua conta.
2. Clique no botão **New** (ou acesse [github.com/new](https://github.com/new)).
3. Defina o nome do repositório (exemplo: `biblioteca-django`).
4. Escolha **Público** ou **Privado**.
5. **Atenção:** **NÃO** marque a opção "Add a README file" nem adicione `.gitignore`, pois já temos esses arquivos no projeto.
6. Clique em **Create repository**.

### Passo 7: Conectar o Repositório Local ao GitHub
Copie o link HTTPS fornecido pelo GitHub e execute:
```bash
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```
*(Substitua pela sua URL real).*

### Passo 8: Enviar os Arquivos para o GitHub
```bash
git push -u origin main
```

---

### 💡 Como Fazer Commits no Dia a Dia (Rotina de Atualizações)
Sempre que você fizer alterações no código e quiser salvar no GitHub:
```bash
git status                    # 1. Veja o que mudou
git add .                     # 2. Adicione as mudanças
git commit -m "sua mensagem"  # 3. Descreva o que você fez
git push                      # 4. Envie para o GitHub
```

---

## 🏛️ Guia de Expansão para a P1: Biblioteca Completa

> **Escopo da P1:**
> Sistema de Biblioteca / Acervo com **Empréstimos**, **Fila de Reserva** e **Cálculo de Multa por Atraso**.
> **Entidades:** `Livro`, `Autor`, `Exemplar`, `Membro`, `Emprestimo`, `Reserva`.

Abaixo está o modelo de arquitetura pronto para você implementar no seu app `acervo`:

### 1. Modelos Completos para a P1 (`acervo/models.py`)

Substitua ou adicione no seu [acervo/models.py](acervo/models.py):

```python
from django.db import models
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal

class Autor(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    ano = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)

    def __str__(self):
        return self.titulo

    @property
    def exemplares_disponiveis(self):
        """Retorna a quantidade de cópias disponíveis para empréstimo."""
        return self.exemplares.filter(status='DISPONIVEL').count()


class Exemplar(models.Model):
    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível'),
        ('EMPRESTADO', 'Emprestado'),
        ('MANUTENCAO', 'Em Manutenção'),
    ]

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='exemplares')
    codigo_patrimonio = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIVEL')

    def __str__(self):
        return f"{self.livro.titulo} (Tombo: {self.codigo_patrimonio})"


class Membro(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"


class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('DEVOLVIDO', 'Devolvido'),
        ('ATRASADO', 'Atrasado'),
    ]

    exemplar = models.ForeignKey(Exemplar, on_delete=models.PROTECT, related_name='emprestimos')
    membro = models.ForeignKey(Membro, on_delete=models.PROTECT, related_name='emprestimos')
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_devolucao_prevista = models.DateField()
    data_devolucao_real = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ATIVO')
    multa = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('0.00'))

    def calcular_multa(self, valor_diario=Decimal('2.00')):
        """
        Calcula a multa caso a devolução ocorra após a data prevista.
        R$ 2,00 por dia de atraso.
        """
        data_referencia = self.data_devolucao_real or timezone.now().date()
        if data_referencia > self.data_devolucao_prevista:
            dias_atraso = (data_referencia - self.data_devolucao_prevista).days
            self.multa = dias_atraso * valor_diario
            if not self.data_devolucao_real:
                self.status = 'ATRASADO'
        else:
            self.multa = Decimal('0.00')
        return self.multa

    def registrar_devolucao(self):
        """Finaliza o empréstimo, calcula multa e libera o exemplar para a fila de reserva."""
        self.data_devolucao_real = timezone.now().date()
        self.calcular_multa()
        self.status = 'DEVOLVIDO'
        self.save()

        # Libera o exemplar
        self.exemplar.status = 'DISPONIVEL'
        self.exemplar.save()

        # Verifica se há reserva esperando na fila
        reserva = Reserva.proxima_reserva(self.exemplar.livro)
        if reserva:
            reserva.status = 'NOTIFICADO'
            reserva.save()

    def __str__(self):
        return f"Empréstimo: {self.exemplar.livro.titulo} para {self.membro.nome}"


class Reserva(models.Model):
    STATUS_CHOICES = [
        ('AGUARDANDO', 'Aguardando na Fila'),
        ('NOTIFICADO', 'Notificado / Disponível para Retirada'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='reservas')
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='reservas')
    data_reserva = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AGUARDANDO')

    class Meta:
        ordering = ['data_reserva']  # Fila FIFO (First In, First Out)

    @classmethod
    def proxima_reserva(cls, livro):
        """Retorna o primeiro membro da fila de reserva para o livro."""
        return cls.objects.filter(livro=livro, status='AGUARDANDO').first()

    def __str__(self):
        return f"Reserva de {self.livro.titulo} para {self.membro.nome} ({self.status})"
```

---

### 2. Regras de Negócio da P1

#### 📌 Fila de Reserva (Lógica FIFO)
1. Quando um membro solicita um livro e **não há exemplares disponíveis** (`exemplares_disponiveis == 0`), cria-se uma instância de `Reserva`.
2. Como a classe `Reserva` tem `ordering = ['data_reserva']`, o banco de dados organiza automaticamente por ordem de chegada.
3. Ao executar `registrar_devolucao()`, o sistema chama `Reserva.proxima_reserva(livro)`. O primeiro da fila recebe o status `NOTIFICADO` para retirar o livro.

#### 📌 Cálculo de Multa por Atraso
1. O método `calcular_multa(valor_diario=Decimal('2.00'))` compara a data de devolução prevista com a devolução real (ou a data atual se ainda não devolvido).
2. Cada dia a mais adiciona R$ 2,00 ao saldo devedor do empréstimo.

---

### 3. Registro no Painel Administrativo (`acervo/admin.py`)

Para que você consiga gerenciar todas as entidades com filtros e buscas:

```python
from django.contrib import admin
from .models import Autor, Livro, Exemplar, Membro, Emprestimo, Reserva

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano', 'exemplares_disponiveis')
    search_fields = ('titulo', 'autor__nome')

@admin.register(Exemplar)
class ExemplarAdmin(admin.ModelAdmin):
    list_display = ('codigo_patrimonio', 'livro', 'status')
    list_filter = ('status',)

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'email', 'ativo')
    search_fields = ('nome', 'matricula')

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('exemplar', 'membro', 'data_emprestimo', 'data_devolucao_prevista', 'status', 'multa')
    list_filter = ('status', 'data_devolucao_prevista')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('livro', 'membro', 'data_reserva', 'status')
    list_filter = ('status',)
```

---

### 4. Como Aplicar a Expansão no seu Projeto
Quando for implementar os novos modelos da P1:
1. Atualize o arquivo `acervo/models.py`.
2. Execute no terminal:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Atualize o `acervo/admin.py` com o código acima.
4. Crie os formulários em `acervo/forms.py` para as entidades desejadas (ex: `EmprestimoForm`, `ReservaForm`).
5. Crie as views e rotas para empréstimo e reserva no `views.py` e `urls.py`.

---

## 👨‍💻 Autor
Projeto desenvolvido para a disciplina de **Laboratório de Programação Full Stack** - Universidade de Vassouras.
Professor: **Márcio Garrido**.
Aluno: **Cauan Ferreira Almeida**.

