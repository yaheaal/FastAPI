from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.src import database, schemas, hashing
from app.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowUser])
def all(db: Session=Depends(get_db)):
    return user.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.User, db: Session=Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def show(id: int, db: Session=Depends(get_db)):
    return user.show(id, db)