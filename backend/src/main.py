from fastapi import FastAPI
from src.config.manager import settings

backend_app = FastAPI()

@backend_app.get("/")
def read_root():
    return {"Hello": "form docker compose"}

print(settings) 