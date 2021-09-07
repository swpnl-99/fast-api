from passlib.context import CryptContext


class Hash():
    def crypt(password : str):
        pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated = "auto")
        hashed_password = pwd_cxt.hash(password)
        return hashed_password
    
    def verify(hashed_password, plain_password):
        pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated = "auto")        
        return pwd_cxt.verify(plain_password,hashed_password)
