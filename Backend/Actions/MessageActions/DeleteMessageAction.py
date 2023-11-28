from Database import FireBaseDatabase
from firebase_admin import firestore
from google.cloud.exceptions import NotFound

def deleteMessage(message_id, chatroom_id):
    db = FireBaseDatabase.getConnection()

    chatroom_message_ref = db.child("Chatroom Messages").child(chatroom_id).child(message_id)
    if chatroom_message_ref is None:
        FireBaseDatabase.closeConnection()
        raise Exception("There is no message with that id")
    chatroom_message_ref.delete()

    FireBaseDatabase.closeConnection()
