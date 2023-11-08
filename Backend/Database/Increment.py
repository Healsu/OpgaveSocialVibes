from firebase_admin import firestore

def getLatestDocument(db, CollectionName):
    print("Gettign Latest Document")
    try:
        collection_ref = db.collection(CollectionName)
        query = collection_ref.order_by('TimeStamp', direction=firestore.Query.DESCENDING).limit(1)
        results = query.stream()
        latest_doc = next(results)
        data = latest_doc.to_dict()
        return int(data["ID"])
    except:
        print("There are no existing docs, set value to 0")
        return 0
    