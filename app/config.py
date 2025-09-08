import os

# 'basedir' aponta para a pasta 'app'
basedir = os.path.abspath(os.path.dirname(__file__))
# 'root_dir' aponta para a pasta raiz do projeto (um nível acima da 'app')
root_dir = os.path.dirname(basedir)

class Config:
    """Configurações da aplicação."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    db_path = os.path.join(root_dir, 'app', 'database', 'reviews.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False