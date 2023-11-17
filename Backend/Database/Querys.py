from firebase_admin import firestore
from google.cloud import firestore
from google.cloud.exceptions import NotFound

#Helper methods for the different actions that can be usefull for multiple actions

def getById(db, CollectionName, id):
    print("Gettign object by id")
    
    ref = db.child(CollectionName)

    
    data = ref.child(id).get()
    data["id"] = id


    if(not data):
        raise Exception(f"There are no existing entity with that id: {id}")
    return data

    
def addChatroomIdToParticipantsProfile(db, chatroom_id, participants, isDelete):
    #id parameter is the chatroom parameter
    #participants need to be a list
    print("Adding Chatroom IDs to Profiles")
    try:
        collection_ref = db.collection("Profiles")
        #finds where profile with an id like the participants are and gets their profile
        #uses the data to append the chatroom id to the chatroom array on their profiles or remove the id from their profiles
        for profile in participants:
            doc_ref = collection_ref.document(profile)
            if not isDelete:
                doc_ref.update({
                    'ChatRoomIds': firestore.ArrayUnion([chatroom_id])
                })
            else:
                doc_ref.update({
                    'ChatRoomIds': firestore.ArrayRemove([chatroom_id])
                })       
    except:
        print("One of the participant Ids dosen't exist")
        return None

    
