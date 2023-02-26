from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser


def create_user(db : Session, request : UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        
    )