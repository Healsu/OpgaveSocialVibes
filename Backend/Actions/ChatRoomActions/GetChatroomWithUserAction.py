from Database import FireBaseDatabase, Querys

def userInChatroom(user_id):
    try:
        db = FireBaseDatabase.getConnection()
        chatrooms = db.child("Chatroom Participants").get().items()
        chatroom_objects = {}
        for chatroom in chatrooms:
            for profile in chatroom[1]:
                if(profile["id"] == user_id):
                    chatroom_data = db.child("Chatrooms").child(chatroom[0]).get()
                    data = {
                        'ChatroomID': chatroom[0],
                        'Latest Message': chatroom_data.get("Latest Message", None),
                        'TimeStamp': chatroom_data.get("TimeStamp", None),
                        'Title': chatroom_data.get("Title", None),
                        'Type': chatroom_data.get("Type", None)
                    }

                    chatroom_objects[chatroom[0]] = data 
        FireBaseDatabase.closeConnection()
        return chatroom_objects
    except:
        FireBaseDatabase.closeConnection()