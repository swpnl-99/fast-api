from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from Blog import models
from fastapi import APIRouter, status, HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from .. import schemas, hashing
from ..database import get_db
from ..token import create_access_token

router  = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request : OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.user).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    if not hashing.Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
