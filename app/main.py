from random import randrange
from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
# from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor 
from sqlalchemy.orm import Session
import time
from . import models, schemas
from .database import engine, get_db


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




# my_posts = [{"title":"title of post 1", "content":"content of post 1", "id":1},
#              {"title":"title of post 2", "content":"content of post 2","id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id']==id:
#             return i


@app.get("/")
def root():
    return {"message":"Welcome to my api"}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts= db.query(models.Post).all()
    return {"data":posts}


@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING * """
    #                ,(post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post}

@app.get("/posts/{id}")
def get_post(id:int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """,(str(id)))
    # post = cursor.fetchone()
    post= db.query(models.Post).filter(models.Post.id==  id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id {id} was not found.")
        
    return {"post detail":post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id== id)

    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id:int,updated_post:schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published= %s WHERE id = %s RETURNING *"""
    #                ,(post.title,post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query= db.query(models.Post).filter(models.Post.id== id)
    post=post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return {'data':updated_post}
