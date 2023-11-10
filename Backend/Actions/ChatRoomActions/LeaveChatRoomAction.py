from Database import FireStore, Querys
from google.cloud.firestore_v1.base_query import FieldFilter

def leave(chatroom_id, user_id):
    collectionName = 'Chatrooms'
    db = FireStore.getConnection()
    collection = db.collection(collectionName)

    #get the chatroom docs
    chatroom_data, chatroom_doc_id = Querys.getById(db, collectionName, chatroom_id)

    #get the field with profile ids from the dictionary
    participants = chatroom_data['ParticipantsId']

    #the array needed for the chatroom to change:
    participants.remove(user_id)
    print(participants)
    #Remove from the chatroom
    collection.document(chatroom_doc_id).update({'ParticipantsId': chatroom_data['ParticipantsId']})

    #Remove from the profile chatroom list, inverted since it removes everything inside the list so can't use the participants list here
    Querys.addChatroomIdToParticipantsProfile(db, chatroom_data['ID'], [user_id], True)
    FireStore.closeConnection()