from Database import FireStore, Querys
from google.cloud.firestore_v1.base_query import FieldFilter

def addUser(id, user_id):
    db = FireStore.getConnection()
    collectionName = 'Chatrooms'
    collection = db.collection(collectionName)

    #get the chatroom docs
    chatroom_data, chatroom_id = Querys.getById(db, collectionName, id)
    #check so the id isen't already in the list
    contains_user_id = chatroom_data['ParticipantsId'].count(user_id)

    if contains_user_id == 0:
        chatroom_data['ParticipantsId'].append(user_id)
        collection.document(chatroom_id).update({'ParticipantsId': chatroom_data['ParticipantsId']})
        #add chatroom id to profile chatroom list
        Querys.addChatroomIdToParticipantsProfile(db, chatroom_data['ID'],chatroom_data['ParticipantsId'], False)

        FireStore.closeConnection()
    else:
        FireStore.closeConnection()
        raise Exception("The user already exist in the chatroom")

        

    

    