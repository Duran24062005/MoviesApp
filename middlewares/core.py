# middleware/core.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:5500"],  # Permitir el origen de tu frontend
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )