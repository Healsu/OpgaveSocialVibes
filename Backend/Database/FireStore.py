from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, firestore
load_dotenv()

def getConnection():
    cred = credentials.Certificate(os.getenv('DB_CRED'))
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    return db
def closeConnection():
    firebase_admin.delete_app(firebase_admin.get_app())