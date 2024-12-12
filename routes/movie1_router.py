from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from db import movies_table
from schemas.movies_schema import Movie as MovieEntity
from schemas.movies_schema import MovieUpdate as MovieUpdateEntity
from schemas.movies_schema import MovieCreate as MovieCreateEntity
from config.database import Session
from services.movies_service import MovieService

movie1_router = APIRouter()

# HTMLResponse()
@movie1_router.get('/', tags=['App 1'], status_code=200, response_description='Ruta de raíz')
async def home():
    return HTMLResponse("<h1>Welcome to the Movies API</h1>")

# PlainTextResponse()
@movie1_router.get('/plaintext', tags=['App 1'])
async def plaintext():
    return PlainTextResponse("This is Endpoint for text plain send")

# RedirecResponse()
@movie1_router.get('/redirectresponse', tags=['App 1'])
async def redirectresponse():
    return RedirectResponse(url="/", status_code=303)

# FileResponse()
@movie1_router.get('/fileresponse', tags=['App 1'])
async def fileresponse():
    return FileResponse("files/C++ 2 Sticker _ Programming.jpeg")

# JSONResponse()
@movie1_router.get('/movies', tags=['Movies 1'], status_code=200, response_model=list)
async def get_movies()->list[MovieEntity]:
    return JSONResponse(status_code=200, content=movies_table)

@movie1_router.get('/movies/database', tags=['Movies 1'], status_code=200, response_model=list)
async def get_movies()->list[MovieEntity]:
    db = Session()
    resp = MovieService(db).get_movies()
    db.close()
    return JSONResponse(status_code=200, content=resp)



# Paramtros de ruta
@movie1_router.get('/movies/{id}', tags=['Movies 1'], status_code=404)
async def get_movie(id: int = Path(gt=0))->MovieEntity | dict:
    for movie in movies_table:
        if movie['id'] == id:
            return movie
    response = {"error": "Movie not found"}
    return JSONResponse(content=response, status_code=404)

# Paeametros query
@movie1_router.get('/movies/', tags=['Movies 1'])
async def get_movie_by_category(category: str = Query(min_length=5, max_length=20))->list[MovieEntity] | dict:
    movies = []
    for movie in movies_table:
        if movie['category'].lower() == category.lower():
            movies.append(movie)
    if movies:
        return movies
    return {"Error": " Catagory not found."}

@movie1_router.post('/movie', tags=['Movies 1'])
async def create_movie(movie: MovieCreateEntity)->MovieCreateEntity:
    if movie:
        movies_table.append(movie.model_dump())
        return JSONResponse(content={"Created": "successfully"}, status_code=201)
    respons = {"Error": "Movie not created"}
    return JSONResponse(content=respons, status_code=400)

@movie1_router.put('/movie/{id}', tags=['Movies 1'])
async def update_movie(id: int, updated_movie: MovieUpdateEntity) -> MovieEntity | dict:
    for existing_movie in movies_table:
        if existing_movie['id'] == id:
            existing_movie.update(updated_movie.model_dump())
            return updated_movie.model_dump()
    return {"Error": "Movie not found"}

    
@movie1_router.delete('/movie/{id}', tags=['Movies 1'])
async def delete_movie(id: int)->dict:
    for existing_movie in movies_table:
        if existing_movie['id'] == id:
            movies_table.remove(existing_movie)
            return {"Deleted": "successfully"}
    response = {"Error": "Movie not deleted"}
    return JSONResponse(content=response, status_code=404)
