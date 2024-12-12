from models.movies_model import Movie as MoviEntity

class MovieService():

    def __init__(self, db) -> None:
        self.db = db

    
    def get_movies(self):
        result = self.db.query(MoviEntity).all()
        return result
    
    def create_movies(self)