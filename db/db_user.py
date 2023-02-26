from sqlalchemy.orm.session import Session
from db.hash import Hash
from schemas import UserBase
from db.models import DbUser


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
    return db.query(DbUser).filter(DbUser.id==id).first()

