from Database import FireBaseDatabase

def add(chatroom_id, message_id, reaction):
    db = FireBaseDatabase.getConnection()
    
    message_ref = db.child("Chatroom Messages").child(chatroom_id).child(message_id).child("Reactions")

    #check if there is a reactions Dictionary already
    if( message_ref.get() is None ): #it dosen't have one so create a new one

        message_ref.child(reaction).set(1)
        
    else: #It has one so just append to it
        if( message_ref.child(reaction).get() is None ): #the key dosen't exist in the one that already exists so create a new key
            print("That reaction isen't in the dict")
            message_ref.child(reaction).set(1)

        else: #the key exists so just increment the value
            count = message_ref.child(reaction).get()
            message_ref.child(reaction).set(count+1)
            print("Incremented the choosen reaction")

    FireBaseDatabase.closeConnection()