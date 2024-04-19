from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://hackathon-undefined.ru:80",
    "http://hackathon-undefined.ru:8000",
    "http://localhost:80",
    "http://localhost:8000",
    "http://127.0.0.1:80",
    "http://127.0.0.1:8000",
    "80.242.57.199",
    "80.242.57.199:8000",
    "80.242.57.199:80",
    "http://80.242.57.199:80",
    "http://80.242.57.199:8000",
    "http://hackathon-undefined.ru/",
    "http://hackathon-undefined.ru",
    "hackathon-undefined.ru:8000",
    "hackathon-undefined.ru:80",
    "hackathon-undefined.ru"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "Hello World <3 <3"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
