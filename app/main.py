import os
from typing import Optional, List
from fastapi import Body, FastAPI
from . import models
import sqlalchemy
from .database import engine
from .routers import post, user, auth, vote 
from fastapi.middleware.cors import CORSMiddleware
from alembic.config import Config
from alembic.command import upgrade
from pathlib import Path
from database import metadata, database
from .config import settings

app = FastAPI()
app.state.database = database

@app.on_event("startup")
async def startup() -> None:
    """Startup application."""
    database_url = f'{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
    db_url = os.getenv(database_url)
    db_path = db_url.replace("postgresql://", "")
    if not Path(db_path).exists():
        engine = sqlalchemy.create_engine(db_url)
        metadata.drop_all(engine)
        metadata.create_all(engine)

    upgrade(Config(), "head")

    database = app.state.database
    if not database.is_connected:
        await database.connect()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message":"Welcome to my api"}



