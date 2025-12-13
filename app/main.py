from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Notes API")

class NoteSchema(BaseModel):
    title: str
    content: str


@app.post("/notes/")
def create_note():
    pass


@app.get("/notes/")
def read_notes():
    pass

