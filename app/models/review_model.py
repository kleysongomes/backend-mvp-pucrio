from app import db
import datetime

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    
    last_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        """
        Retorna uma representação em string do objeto Review, útil para depuração.
        Exemplo: <Review 1 'Estudo de Gênesis 1'>
        """
        return f"<Review {self.id} '{self.title}'>"

    def to_json(self):
        """
        Converte o objeto Review para um dicionário (formato JSON).
        """
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'date_posted': self.date_posted.isoformat(),
            'last_updated': self.last_updated.isoformat() # Adicionado aqui
        }