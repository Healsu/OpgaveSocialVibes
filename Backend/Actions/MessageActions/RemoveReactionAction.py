from Database import FireBaseDatabase

def remove(chatroom_id, message_id, reaction, user_id):
    db = FireBaseDatabase.getConnection()
    
    message_ref = db.child("Chatroom Messages").child(chatroom_id).child(message_id).child("Reactions")

    #check if there is a reactions Dictionary
    if( message_ref.get() is None ): #it dosen't have one so create a new one
        raise Exception("There are no reactions for this message to delete")
    
    #the key dosen't exist in the one that already exists so create a new key
    if( message_ref.child(reaction).get() is None ): 
        raise Exception("That reaction isen't in the dict to be deleted")
    
    count = message_ref.child(reaction).child("Count").get()
    users = message_ref.child(reaction).child("Users").get()
    #check if the user is has made that reaction
    if( user_id not in users ):
        raise Exception("That user haven't made that reaction")

    #the key exists so just increment the value
    if( count > 1 ): 
        message_ref.child(reaction).child("Count").set(count-1)
        users.remove(user_id)
        message_ref.child(reaction).child("Users").set(users)
    else: #removes the child from the database if the count is 0
        message_ref.child(reaction).delete()


    FireBaseDatabase.closeConnection()