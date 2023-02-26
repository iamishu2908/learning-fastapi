from pydantic import BaseModel

class UserBase(BaseModel):
    username : str
    email : str
    password : str

class UserDisplay(BaseModel):
    username:str
    email:str
    class Config():
        orm_mode = True #allows system to database data automaticialy inthe format we give
        #without this we cannot convert frim one datatype to other