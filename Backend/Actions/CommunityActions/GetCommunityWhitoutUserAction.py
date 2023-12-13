from Database import FireBaseDatabase, Querys


def get(user_id):
    db = FireBaseDatabase.getReferenceFromConnection("Chatrooms")
    
    # Query to get all chatrooms where the type is equal to 'Community'
    query_result = db.order_by_child("Type").equal_to("Community").get()
    
    FireBaseDatabase.closeConnection()
    

    db = FireBaseDatabase.getConnection()
    chatroom_keys = {}
    user_object = Querys.getById(db, "Profiles", user_id)
    
    for key, value in query_result.items():
        participants_list = db.child("Chatroom Participants").child(key).get()

        if( user_object not in participants_list):
            chatroom_keys[key] = value
    
    return chatroom_keys
