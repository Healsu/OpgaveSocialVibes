import os
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(os.environ['DB_CRED'])
firebase_admin.initialize_app(cred)

db = firestore.client()

