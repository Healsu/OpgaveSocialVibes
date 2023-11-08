from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

def getById(db, CollectionName, id):
    print("Gettign object by id")
    try:
        collection_ref = db.collection(CollectionName)
        query = collection_ref.where(filter=FieldFilter('ID', "==", id))
        results = query.stream()
        latest_doc = next(results)
        data = latest_doc.to_dict()
        doc_id = latest_doc.id
        return data, doc_id
    except:
        print("There are no existing docs with that id")
        return None
    
