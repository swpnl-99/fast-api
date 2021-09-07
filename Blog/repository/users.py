from sqlalchemy.orm.session import Session
from Blog import schemas
from fastapi import HTTPException, status
from .. import models, hashing


def create_user(request : schemas.User, db:Session):
    new_user = models.User(name = request.name, email = request.email, password = hashing.Hash.crypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int , db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"User with the id {id} not found")
    return user