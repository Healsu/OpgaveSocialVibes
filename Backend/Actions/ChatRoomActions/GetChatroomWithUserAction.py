from Database import FireStore

def userInChatroom(user_id):
    db = FireStore.getConnection()
    chatrooms = db.child("Chatroom Participants").get().items()
    chatroom_ids = []
    for chatroom in chatrooms:#sort the chatrooms
        for profile in chatroom[1]:#sort out profiles from the chatroom
            if(profile["id"] == user_id):#sort for user id in the chatroom
                chatroom_ids.append(chatroom[0])#append the id to the return array

    FireStore.closeConnection()
    
    return chatroom_ids