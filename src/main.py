from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main_get():
    return {'message' : 'hello world'}