from passlib.context import CryptContext

pwd_context = CryptContext(schemes='bcrypt',deprecated = 'auto')

class Hash():
    def brcypt(password:str):
        return pwd_context.hash(password)
    
    def verify(hashed_password, plain_password):# to check whether a pass provided is a correct one in authentication
        return pwd_context.verify(plain_password,hashed_password)