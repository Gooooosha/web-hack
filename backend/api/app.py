from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello World <3 <3"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
