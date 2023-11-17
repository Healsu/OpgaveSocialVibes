from Database import FireStore, Querys
from Model.Message import Message
from firebase_admin import firestore

def SendMessage(chatroom_id, message, senderId):
    db = FireStore.getConnection()

    
    
    #check if the chatroom id exist
    chatroom_ref = db.child("Chatrooms").child(chatroom_id).get()
    if chatroom_ref is None:
        FireStore.closeConnection()
        raise Exception("There is no chatroom with that id")
    
    #create the message object
    message = Message(message, senderId)

    chatroom_messages_ref = db.child("Chatroom Messages").child(chatroom_id).push(message.toDict())

    FireStore.closeConnection()