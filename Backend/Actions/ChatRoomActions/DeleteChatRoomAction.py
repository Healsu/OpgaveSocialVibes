from Database import FireStore, Querys
from google.cloud.firestore_v1.base_query import FieldFilter

def deleteChatroom(id):
    db = FireStore.getConnection()
    collection = db.collection('Chatrooms')
    #get the chatroom docs
    query = collection.where(filter=FieldFilter('ID', "==", id))
    docs = query.stream()
    #transform the query into data, dictionary specificly
    data = next(docs).to_dict()
    #get the field with profile ids from the dictionary
    participants = data['ParticipantsId']

    #Removed this id from all of the profiles that had this chatroom
    Querys.addChatroomIdToParticipantsProfile(db, id, participants, True)

    #delete the docs from the collection
    docs_to_delete = query.stream()
    for doc in docs_to_delete:
        doc.reference.delete()
    FireStore.closeConnection()