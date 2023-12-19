from firebase_admin import firestore
from google.cloud import firestore
from google.cloud.exceptions import NotFound

#Helper methods for the different actions that can be usefull for multiple actions

def getById(db, CollectionName, id):
    print("Getting object for id:", id)

    if id == "System":
        print("This is a system user")
        return "System"

    ref = db.child(CollectionName)
    
    data = ref.child(id).get()

    if data is None:
        raise Exception(f"There is no existing entity with that id: {id}")

    return data
