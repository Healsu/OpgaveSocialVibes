from Database import FireBaseDatabase, Querys

def userInChatroom(user_id):
    try:
        db = FireBaseDatabase.getConnection()
        chatrooms = db.child("Chatroom Participants").get().items()
        chatroom_objects = {}
        for chatroom in chatrooms:#sort the chatrooms
            for profile in chatroom[1]:#sort out profiles from the chatroom
                if(profile["id"] == user_id):#sort for user id in the chatroom
                    chatroom_data = db.child("Chatrooms").child(chatroom[0]).get()
                    data = {
                        'LastMessage': chatroom_data.get("Last Message", None),
                        'TimeStamp': chatroom_data.get("TimeStamp", None),
                        'Title': chatroom_data.get("Title", None),
                        'Type': chatroom_data.get("Type", None)
                    }

                    chatroom_objects[chatroom[0]] = data #append the chatroom to the return array
        FireBaseDatabase.closeConnection()
        return chatroom_objects
    except:
        FireBaseDatabase.closeConnection()