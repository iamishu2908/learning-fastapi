from db.database import Base
from sqlalchemy import Column, Integer, String

class DbUser(Base): #inheritance of class Base
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,index=True) #automatically generates unique index for every new id
    username = Column(String)
    email = Column(String)
    password = Column(String)# password will be hashed here so that noone will have access to it even if they look into the db
    