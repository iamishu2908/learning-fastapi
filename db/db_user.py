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