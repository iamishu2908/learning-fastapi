from pydantic import BaseModel
from typing import List

#article inside user display
class Article(BaseModel):
    title: str
    content:str
    published:bool
    class Config():
        orm_mode = True

class UserBase(BaseModel):
    username : str
    email : str
    password : str


class UserDisplay(BaseModel):
    username:str
    email:str
    items : List[Article] = []
    class Config():
        orm_mode = True #allows system to database data automaticialy inthe format we give
        #without this we cannot convert frim one datatype to other

# user inside ArticleDisplay
class User(BaseModel):
    id:int
    username:str
    class Config():
        orm_mode=True

class ArticleBase(BaseModel):# arctile received from user
    title: str
    content:str
    published:bool
    creator_id:int

class ArticleDisplay(BaseModel):
    title: str
    content:str
    published:bool
    user : User
    class Config():
        orm_mode = True


