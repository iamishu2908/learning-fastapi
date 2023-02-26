from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.orm import relationship

class DbUser(Base): #inheritance of class Base
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,index=True) #automatically generates unique index for every new id
    username = Column(String)
    email = Column(String)
    password = Column(String)# password will be hashed here so that noone will have access to it even if they look into the db
    items = relationship('DbArticle',back_populates = 'user')
    
class DbArticle(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key= True, index = True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('DbUser',back_populates='items')