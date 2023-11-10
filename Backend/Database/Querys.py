from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from google.cloud import firestore

#Helper methods for the different actions that can be usefull for multiple actions

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
    
def addChatroomIdToParticipantsProfile(db, id, participants, isDelete):
    #id parameter is the chatroom parameter
    #participants need to be a list
    print("Adding Chatroom IDs to Profiles")
    try:
        collection_ref = db.collection("Profiles")
        #finds where profile with an id like the participants are and gets their profile
        query = collection_ref.where(filter=FieldFilter("ID", "in", participants))
        results = query.stream()
        #uses the data to append the chatroom id to the chatroom array on their profiles or remove the id from their profiles
        for doc in results:
            doc_ref = db.collection('Profiles').document(doc.id)
            if(isDelete == False):
                doc_ref.update({
                    'ChatRoomIds': firestore.ArrayUnion([id])
                })
            else:
                doc_ref.update({
                    'ChatRoomIds': firestore.ArrayRemove([id])
                })
        
    except:
        print("One of the participant Ids dosen't exist")
        return None

    
