from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Note
from sqlalchemy import select

app = FastAPI(title="Notes API")

class NoteSchema(BaseModel):
    title: str
    content: str


@app.post("/notes/")
async def create_note(note: NoteSchema, db: AsyncSession = Depends(get_db)):
    new_note = Note(title=note.title, content=note.content)
    db.add(new_note)
    await db.commit()
    await db.refresh(new_note)
    return new_note


@app.get("/notes/")
async def read_notes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Note))
    return result.scalars().all()

