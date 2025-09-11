import sys
from dotenv import load_dotenv
from app import create_app, db
from app.models.review_model import Review

load_dotenv()

# Cria a instância do app para termos o contexto necessário
app = create_app()

# Verificamos se o argumento 'init-db' foi passado ao executar o script
# Exemplo: python manage.py init-db
if len(sys.argv) > 1 and sys.argv[1] == 'init-db':
    # Entra no contexto da aplicação para poder interagir com o banco de dados
    with app.app_context():
        print("Inicializando o banco de dados...")
        
        # O código que cria a pasta 'database' já está no __init__.py,
        
        db.create_all()
        
        print("Banco de dados inicializado com sucesso!")
else:
    # Mensagem de ajuda se nenhum comando válido for passado
    print("Comando inválido.")
    print("Use 'python manage.py init-db' para criar as tabelas do banco de dados.")