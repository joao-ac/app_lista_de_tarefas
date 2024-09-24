# app_lista_de_tarefas

Um simples gerenciador de tarefas desenvolvido em Python usando o framework Flask e o banco de dados SQLite. Este projeto permite que os usuários adicionem, visualizem, atualizem e excluam tarefas, além de incluir uma descrição opcional para cada tarefa.

## Funcionalidades

- Adicionar novas tarefas com título e descrição
- Listar todas as tarefas criadas
- Marcar tarefas como concluídas ou pendentes
- Excluir tarefas
- Expandir e contrair a visualização de descrições de tarefas

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web utilizado para criar a aplicação.
- **SQLite**: Banco de dados leve utilizado para armazenar as tarefas.
- **HTML/CSS**: Estrutura e estilo da interface do usuário.
- **JavaScript**: Interatividade na visualização de tarefas.

## Pré-requisitos

Antes de executar o projeto, você precisará ter o Python e o pip instalados em seu sistema. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

## Instalação

1. Clone este repositório para sua máquina local:
   ```bash
    git clone https://github.com/joao-ac/app_lista_de_tarefas.git

2. Navegue até o diretório do projeto:
   ```bash
   cd app_lista_de_tarefas

4. Crie um ambiente virtual (opcional, mas recomendado): 
    ```bash
    python -m venv venv 
    venv\Scripts\activate  # No windows
    source venv/bin/activate  # No Linux ou MacOS

5. Instale as dependências necessárias:
    ```bash
    pip install Flask Flask-SQLAlchemy

6. Execute a aplicação: 
    ```bash
    python app.py

7. Acesse a aplicação em seu navegador: 
    ```bash
    http://127.0.0.1:5000/
