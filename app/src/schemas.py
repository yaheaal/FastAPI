from pydantic import BaseModel
from typing import List, Optional


class BlogBase(BaseModel):
    user_id: int
    title: str
    body: str


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(UserBase):
    class Config():
        orm_mode = True
    

class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[Blog]
    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None