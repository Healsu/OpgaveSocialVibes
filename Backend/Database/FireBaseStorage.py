import os
from dotenv import load_dotenv
from firebase_admin import credentials, storage
import firebase_admin

load_dotenv()

app = None
bucket = None

def getConnection():
    global app, bucket
    if app is None:
        cred = credentials.Certificate(os.getenv('DB_CRED'))
        app = firebase_admin.initialize_app(cred, { 'storageBucket' : 'social-vibes-4d1d6.appspot.com' })
        bucket = storage.bucket(app=app)
    return bucket

def closeConnection():
    global app
    firebase_admin.delete_app(app)
    app = None