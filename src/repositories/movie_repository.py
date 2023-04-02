from src.models import db, Movie

class MovieRepository:

    def get_all_movies(self):
        all_movies = db.session.query(Movie).all()
        return all_movies

    def get_movie_by_id(self, movie_id):
        movie = db.session.query(Movie).filter_by(movie_id=movie_id).first()
        return movie

    def create_movie(self, title, director, rating):
        new_movie = Movie(title=title, director=director, rating=rating)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        found_movies = db.session.query(Movie).filter(Movie.title.ilike(f"%{title}%")).all()
        return found_movies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
