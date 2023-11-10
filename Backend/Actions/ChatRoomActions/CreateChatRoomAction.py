from Model.Chatroom import Chatroom
from Database import FireStore, Increment, Querys

def craeteChatroom(data):
    collectionName = 'Chatrooms'
    admin = data["Admin"]
    participants = data["Participants"]

    db = FireStore.getConnection()
    collection = db.collection(collectionName)
    #Auto increment the id for chatroom
    latestDocContentID = Increment.getLatestDocument(db, collectionName)
    id = str(latestDocContentID+1)
    #craete the chatroom object
    chatroom = Chatroom(id, participants, admin)
    #add the chatroom id to the participants profiles
    Querys.addChatroomIdToParticipantsProfile(db, id, participants, False)

    collection.document().set(
        chatroom.toDict()
    )

    FireStore.closeConnection()