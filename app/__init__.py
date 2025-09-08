from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from .config import Config
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    
    db.init_app(app)

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API de Reviews de Estudos Bíblicos",
            "description": "API para postar e gerenciar reviews de estudos da Bíblia.",
            "version": "1.0.0"
        },
        "definitions": {
            "ReviewInput": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "example": "Estudo de Gênesis 1"},
                    "content": {"type": "string", "example": "Hoje estudei a criação..."}
                },
                "required": ["title", "content"]
            },
            "ReviewOutput": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "content": {"type": "string"},
                    "date_posted": {"type": "string", "format": "date-time"}
                }
            }
        }
    }

    Swagger(app, config=swagger_config, template=swagger_template)

    from .routes.review_routes import review_bp
    app.register_blueprint(review_bp, url_prefix='/api')

    return app