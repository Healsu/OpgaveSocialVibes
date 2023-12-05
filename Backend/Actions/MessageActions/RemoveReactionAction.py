from Database import FireBaseDatabase

def remove(chatroom_id, message_id, reaction):
    db = FireBaseDatabase.getConnection()
    
    message_ref = db.child("Chatroom Messages").child(chatroom_id).child(message_id).child("Reactions")

    #check if there is a reactions Dictionary
    if( message_ref.get() is None ): #it dosen't have one so create a new one
        raise Exception("There are no reactions for this message to delete")
        
    else: #It has one so just append to it
        if( message_ref.child(reaction).get() is None ): #the key dosen't exist in the one that already exists so create a new key
            print("That reaction isen't in the dict")
            raise Exception("That reaction isen't in the dict to be deleted")

        else: #the key exists so just increment the value
            count = message_ref.child(reaction).get()
            if( count > 1 ): 
                message_ref.child(reaction).set(count-1)
            else: #removes the child from the database if the count is 0
                message_ref.child(reaction).delete()
            print("Decremented the choosen reaction")

    FireBaseDatabase.closeConnection()