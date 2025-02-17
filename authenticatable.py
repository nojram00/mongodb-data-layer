from .base import BaseMongoModel
from .session import Session
import bcrypt

def validate_password(password : str, hashed_password : str):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

def hash_password(password : str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

class AuthenticatableModel(BaseMongoModel):

    collection_name = "users"

    @classmethod
    def login(cls, **credentials):
        password = credentials.pop('password')
        docs = cls.find(credentials)

        if docs is None:
            return None
        
        # Validate Password:
        if not validate_password(password , docs['password']):
            return None
        
        return Session.create_session(docs['_id'])

    @classmethod
    def register(cls, **data):
        data['password'] = hash_password(data['password'])
        return cls.create(**data)
    
    @classmethod
    def logout(cls, session_id):
        Session.remove_session(session_id)