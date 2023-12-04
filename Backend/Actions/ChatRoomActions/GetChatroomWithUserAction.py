from Database import FireBaseDatabase, Querys

def userInChatroom(user_id):
    try:
        db = FireBaseDatabase.getConnection()
        chatrooms = db.child("Chatroom Participants").get().items()
        chatroom_ids = []
        for chatroom in chatrooms:#sort the chatrooms
            for profile in chatroom[1]:#sort out profiles from the chatroom
                if(profile["id"] == user_id):#sort for user id in the chatroom
                    chatroom_ids.append(chatroom[0])#append the id to the return array

        FireBaseDatabase.closeConnection()
        return chatroom_ids
    except:
        FireBaseDatabase.closeConnection()