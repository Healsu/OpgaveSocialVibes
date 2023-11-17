from Model.Chatroom import Chatroom
from Database import FireStore, Querys

def craeteChatroom(data):
    db = FireStore.getConnection()
    participants = data["Participants"]
    admin = Querys.getById(db, "Profiles", data["Admin"])
    

    #craete the data
    chatroom = Chatroom(admin, data["Title"])
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

    FireStore.closeConnection()