from .base import BaseMongoModel
import datetime

class Session(BaseMongoModel):

    collection_name = "sessions"

    @classmethod
    def create_session(cls, user_id):
        return cls.create(
            user_id=user_id,
            date_created=datetime.datetime.now(),
            date_expired=datetime.datetime.now() + datetime.timedelta(days=29)
            )

    @classmethod
    def remove_session(cls, session_id):
        cls.delete(session_id)

    @classmethod
    def validate_session(cls, session_id):
        return cls.find_by_id(session_id) is not None
    
    @classmethod
    def check_session_validity(cls, session_id):
        session = cls.find_by_id(session_id)
        if session is None:
            return False
        return session['date_expired'] > datetime.datetime.now()
    
    @classmethod
    def remove_expired_sessions(cls):
        cls.delete_many({'date_expired': {'$lt': datetime.datetime.now()}})