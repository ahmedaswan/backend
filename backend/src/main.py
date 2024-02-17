from fastapi import FastAPI

backend_app = FastAPI()

@backend_app.get("/")
def read_root():
    return {"Hello": "form docker compose"}

''' 
curl -X 'GET' \
  'http://localhost:8000/' \
  -H 'accept: application/json'\
  -H 'Content-Type: application/json'
'''
# curl -X 'GET' 'http://localhost:8000/' -H 'Content-Type: application/json' -d ''