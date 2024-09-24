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
    git clone https://github.com/seu-usuario/gerenciador-de-tarefas.git

2. Navegue até o diretório do projeto: 
    cd gerenciador-de-tarefas

3. Crie um ambiente virtual (opcional, mas recomendado): 
    python -m venv venv 
    venv/bin/activate

4. Instale as dependências necessárias:
    pip install Flask Flask-SQLAlchemy

5. Execute a aplicação: 
    python app.py

6. Acesse a aplicação em seu navegador: 
    http://127.0.0.1:5000/