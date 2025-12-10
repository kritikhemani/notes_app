from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Notes API")


@app.post("/notes/")
def create_note():
    pass


@app.get("/notes/")
def read_notes():
    pass

