from sqlalchemy.orm.session import Session
from db.hash import Hash
from schemas import UserBase
from db.models import DbUser

from fastapi import HTTPException,status


def create_user(db : Session, request : UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.brcypt(request.password)
    )
    db.add(new_user)
    db.commit()# this sends the operation to the database
    db.refresh(new_user)# daabase usually autogenerates a user detail.sp performing refresh will update the value on both ends correctly
    return new_user

def get_all_users(db:Session):
    return db.query(DbUser).all()# read all users from table

def get_user(db:Session, id:int):
    user = db.query(DbUser).filter(DbUser.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail =f'User with id {id} not found')
    return user


def update_user(db:Session,id:int,request:UserBase):
    user = db.query(DbUser).filter(DbUser.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail =f'User with id {id} not found')
    user.update({DbUser.username:request.username,
                 DbUser.email:request.email,
                 DbUser.password:Hash.brcypt(request.password)})
    db.commit()
    return 'ok updated'

def delete_user(db:Session,id :int):
    user = db.query(DbUser).filter(DbUser.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail =f'User with id {id} not found')
    db.delete(user)
    db.commit()
    return 'ok deleted'

