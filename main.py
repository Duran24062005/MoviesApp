from fastapi import FastAPI
from middlewares.core import setup_cors
from db import movies_table
from routes.movie1_router import movie1_router
from routes.movies_routes import movies_routes


app = FastAPI()

app.title = "FastAPI App for Movies🌍"
app.description = "This is a simple API for movies🚀"
app.version = "1.0.0"

# Configuración de CORS
setup_cors(app)

app.include_router(movie1_router)
app.include_router(movies_routes)
