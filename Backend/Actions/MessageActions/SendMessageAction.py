from Database import FireBaseDatabase, FireBaseStorage, Querys
from Model.Message import Message
from firebase_admin import firestore
from WebSocket.Extensions import socketio, emit, join_room, leave_room
from werkzeug.utils import secure_filename
import uuid
import os

def SendMessage(chatroom_id, message, senderId, message_image=None):
    unique_filename = None
    message_image_url = None
    if message_image != None:
        print(message, message_image)
        bucket = FireBaseStorage.getConnection()
        #Secure filename protects aginst attack using special characters.
        original_filename = secure_filename(message_image.filename)
        unique_filename = os.path.splitext(original_filename)[0] + str(uuid.uuid4()) + os.path.splitext(original_filename)[1]
        #check if the filename exits in the database
        if( bucket.blob(f"Messages/{unique_filename}").exists() ):
            FireBaseStorage.closeConnection()
            raise Exception("That name already exsists in the database")

        bucket.blob(f"Messages/{unique_filename}").upload_from_file(message_image)

        FireBaseStorage.closeConnection()
    #-------------------------------------------------------------------------------------

    db = FireBaseDatabase.getConnection()
    
    senderObject = Querys.getById(db,"Profiles", senderId)
    #check if the chatroom id exist
    chatroom_ref = db.child("Chatrooms").child(chatroom_id).get()
    if chatroom_ref is None:
        FireBaseDatabase.closeConnection()
        raise Exception("There is no chatroom with that id")
    
    #create the message object
    message = Message(message, senderObject, unique_filename)

    chatroom_messages_ref = db.child("Chatroom Messages").child(chatroom_id).push(message.toDict())
    print(chatroom_id)
    socketio.emit("new_message", message.toDict(), room=chatroom_id)

    #Update latest message in chatroom
    chatroom_ref = db.child(f"Chatrooms/{chatroom_id}").update({"Last Message":message.toDict()})

    FireBaseDatabase.closeConnection()