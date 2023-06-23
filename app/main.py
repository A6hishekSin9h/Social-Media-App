from random import randrange
from typing import Optional, List
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
# from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor 
from sqlalchemy.orm import Session
import time
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth 


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database = 'Social Media App', user= 'postgres',
                            password='passw6767', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    except Exception as error:
        print("Connecting to database failed!")
        print(error)
        time.sleep(2)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message":"Welcome to my api"}



