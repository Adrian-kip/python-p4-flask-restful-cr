# models.py
from extensions import db

class Newsletter(db.Model):
    __tablename__ = 'newsletters'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    published_at = db.Column(db.DateTime, server_default=db.func.now())
    edited_at = db.Column(db.DateTime, onupdate=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'published_at': self.published_at.isoformat() if self.published_at else None,
            'edited_at': self.edited_at.isoformat() if self.edited_at else None
        }