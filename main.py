from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Notes API")

class Note(BaseModel):
    text: str

notes: dict[int, dict] = {}
next_id = 1

@app.get("/health")
def health():
    return {"status": "ok", "service": "notes-api", "version": "2.0.0"}

@app.get("/notes")
def list_notes():
    return list(notes.values())

@app.post("/notes", status_code=201)
def create_note(note: Note):
    global next_id
    saved = {"id": next_id, "text": note.text}
    notes[next_id] = saved
    next_id += 1
    return saved

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes[note_id]
