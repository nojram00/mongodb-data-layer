import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')

if not MONGO_DB_URL or not MONGO_DB_NAME:
    raise ValueError("Please provide MONGO_DB_URL and MONGO_DB_NAME in .env file")

def create_connection():
    client = MongoClient(MONGO_DB_URL)
    db = client[MONGO_DB_NAME]
    return db

if __name__ == "__main__":
    db = create_connection()
    print(db.list_collection_names())