from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")

# Example in-memory data store
items = [
    {"id": 1, "name": "Write Python notes", "done": False},
    {"id": 2, "name": "Practice API routes", "done": True},
]


class ItemCreate(BaseModel):
    name: str
    done: bool = False


class ItemUpdate(BaseModel):
    name: str | None = None
    done: bool | None = None


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI task API!"}


# TODO: Add a GET route to list all items


# TODO: Add a GET route to fetch one item by id


# TODO: Add a POST route to create a new item


# TODO: Add a PUT route to update an item


# TODO: Add a DELETE route to remove an item
