from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, db
load_dotenv()

app = None

def getConnection():
    global app
    if app is None:
        cred = credentials.Certificate(os.getenv('DB_CRED'))
        app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://social-vibes-4d1d6-default-rtdb.europe-west1.firebasedatabase.app//'})
    return db.reference()

def getReferenceFromConnection(reference):
    global app
    if app is None:
        cred = credentials.Certificate(os.getenv('DB_CRED'))
        app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://social-vibes-4d1d6-default-rtdb.europe-west1.firebasedatabase.app//'})
    return db.reference(reference)

def closeConnection():
    global app
    if app is not None:
        firebase_admin.delete_app(app)
    app = None