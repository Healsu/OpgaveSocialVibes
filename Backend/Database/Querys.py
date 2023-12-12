from firebase_admin import firestore
from google.cloud import firestore
from google.cloud.exceptions import NotFound

#Helper methods for the different actions that can be usefull for multiple actions

def getById(db, CollectionName, id):
    print("Gettign object by id")
    if( id is "System"):
        return "System"
    
    ref = db.child(CollectionName)

    
    data = ref.child(id).get()
    data["id"] = id


    if(not data):
        raise Exception(f"There are no existing entity with that id: {id}")

    return data
