# API - Diário de Estudos Bíblicos

## 📖 Descrição do Projeto

Esta é uma API RESTful desenvolvida como parte do MVP do curso de Desenvolvimento Full Stack. O objetivo é fornecer um serviço de back-end para gerenciar reviews de estudos bíblicos. A aplicação permite criar, ler, atualizar, deletar e buscar reviews, com toda a documentação da API gerada dinamicamente com Swagger.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**: Linguagem de programação principal.
* **Flask**: Micro-framework web para a criação da API.
* **Flask-SQLAlchemy**: Para interação com o banco de dados.
* **Flask-CORS**: Para permitir a comunicação com o front-end.
* **Flasgger (Swagger)**: Para documentação interativa da API.
* **SQLite**: Banco de dados relacional baseado em arquivo.

---

## 🚀 Instruções de Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

* Python 3.10 ou superior
* `pip` (gerenciador de pacotes do Python)

### Passos

1.  **Clone o Repositório**
    ```bash
    git clone [https://github.com/SEU_USUARIO/backend-mvp-pucrio.git](https://github.com/SEU_USUARIO/backend-mvp-pucrio.git)
    cd backend-mvp-pucrio
    ```

2.  **Crie e Ative o Ambiente Virtual**
    * No Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as Dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente**
    * Crie uma cópia do arquivo `.env.example` e renomeie para `.env`.
    * Abra o arquivo `.env` e adicione uma chave secreta segura para a variável `SECRET_KEY`.

5.  **Crie o Banco de Dados**
    * Execute o console interativo do Python:
        ```bash
        python
        ```
    * Dentro do console, execute os seguintes comandos para criar as tabelas:
        ```python
        from app import create_app, db
        from app.models.review_model import Review
        app = create_app()
        app.app_context().push()
        db.create_all()
        exit()
        ```

6.  **Inicie o Servidor**
    ```bash
    python app.py
    ```

A API estará rodando em `http://127.0.0.1:5000`.

---

## 📚 Documentação da API (Swagger)

Com o servidor em execução, a documentação completa e interativa da API está disponível em:

[http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/)