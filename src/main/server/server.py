from fastapi import FastAPI
from src.main.routes import routes

app = FastAPI()

app.include_router(routes.router)
