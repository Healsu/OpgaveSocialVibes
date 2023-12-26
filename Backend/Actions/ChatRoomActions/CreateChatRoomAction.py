from Model.Chatroom import Chatroom
from Database import FireBaseDatabase, Querys
from Actions.MessageActions import SendMessageAction
from Model.Message import Message

def craeteChatroom(data):
    db = FireBaseDatabase.getConnection()
    participants = data["Participants"]
    admin = Querys.getById(db, "Profiles", data["Admin"])
    initial_message = Message("Be the first to type", "System")

    #craete the data
    chatroom = Chatroom(admin, data["Title"], initial_message.toDict())
    chatroom.setType(participants)
    participants_objects = []
    messages = []

    for profile in participants:
        profile_data = Querys.getById(db, "Profiles", profile)
        participants_objects.append(profile_data)
    
    #create objects in json database
    chatroom_ref = db.child('Chatrooms')
    
    new_data_ref = chatroom_ref.push(chatroom.toDict())
    
    #get the id for the object
    chatroom_ref_id = new_data_ref.key

    #use it to create the other json objects
    chatroom_participants_ref = db.child('Chatroom Participants')
    chatroom_participants_ref.child(chatroom_ref_id).set(participants_objects)

    FireBaseDatabase.closeConnection()

    #Create the message and send a static message
    SendMessageAction.SendMessage(chatroom_ref_id, initial_message.message, "System")

    return chatroom_ref_id
    #try catch