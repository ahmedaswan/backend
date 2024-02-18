from fastapi import FastAPI
from src.config.manager import settings

from src.securites.hashing.hash import hash_generator
backend_app = FastAPI()

@backend_app.get("/")
def read_root():
    return {"Hello": "form docker compose"}


print(hash_generator.generate_password_salt_hash)
print(hash_generator.generate_password_hash(hash_salt=hash_generator.generate_password_salt_hash, password="password"))
print(hash_generator.verify_password_hash(password="password", hashed_password=hash_generator.generate_password_hash(hash_salt=hash_generator.generate_password_salt_hash, password="password")))