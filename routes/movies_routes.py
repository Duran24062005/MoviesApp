from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.movies_schema import Movie as MovieEntity
from config.database import Session
from services.movies_service import MovieService

movies_routes = APIRouter()

@movies_routes.get('/movies/database', tags=['Movies'], status_code=200, response_model=list)
async def get_movies()->list[MovieEntity]:
    db = Session()
    resp = MovieService(db).get_movies()
    db.close()
    return JSONResponse(status_code=200, content=resp)

@movies_routes.post('/movies', tags=['Movies'])
async def create_movie(movie: MovieEntity):
    db = Session()
    resp = MovieService(db).create_movie(movie)
    db.close()
    return JSONResponse(status_code=201, content=resp)