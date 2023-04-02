# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Movie {self.movie_id}: {self.title} ({self.director}), rating {self.rating}>"