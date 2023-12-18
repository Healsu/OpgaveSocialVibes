from Database import FireBaseDatabase, Querys
from Model.Message import Message
from Model.Chatroom import Chatroom
from Actions.MessageActions import SendMessageAction

def createCommunity(data):
    db = FireBaseDatabase.getConnection()
    admin = Querys.getById(db, "Profiles", data["Admin"])
    initial_message = Message("Be the first to type", "System")

    #craete the chatroom object
    chatroom = Chatroom(admin, data["Title"], initial_message.toDict())
    chatroom.setTypeCommunity()

    #create objects in json database
    chatroom_ref = db.child('Chatrooms')
    
    new_data_ref = chatroom_ref.push(chatroom.toDict())
    
    #get the id for the object
    chatroom_ref_id = new_data_ref.key

    #use it to create the other json objects
    chatroom_participants_ref = db.child('Chatroom Participants')
    chatroom_participants_ref.child(chatroom_ref_id).set([admin])

    FireBaseDatabase.closeConnection()

    SendMessageAction.SendMessage(chatroom_ref_id, initial_message.message, "System")

    