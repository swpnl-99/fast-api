from fastapi import APIRouter,Depends, HTTPException,status
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user
from .. import database,schemas,models,hashing
from ..database import SessionLocal,get_db
from ..repository import users
router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post('/', response_model= schemas.ShowUser, tags=['Users'])
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    return users.create_user(request, db)

@router.get('/{id}', response_model= schemas.ShowUser, tags=['Users'])
def get_user(id: int, db:Session = Depends(get_db)):
    return users.get_user(id, db)

