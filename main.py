from fastapi import FastAPI
from app.routers import blog, user, authentication
from app.src.database import Base, engin

app = FastAPI()

Base.metadata.create_all(engin)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)