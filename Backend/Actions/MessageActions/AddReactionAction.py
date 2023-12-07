from Database import FireBaseDatabase

def add(chatroom_id, message_id, reaction, user_id):
    db = FireBaseDatabase.getConnection()
    
    message_ref = db.child("Chatroom Messages").child(chatroom_id).child(message_id).child("Reactions")

    #check if there is a reactions Dictionary already
    if( message_ref.get() is None ): #it dosen't have one so create a new one

        message_ref.child(reaction).set({
            "Count": 1,
            "Users": [
                user_id
            ]
        })
        
    else: #It has one so just append to it
        if( message_ref.child(reaction).get() is None ): #the key dosen't exist in the one that already exists so create a new key
            print("That reaction isen't in the dict")
            message_ref.child(reaction).set({
            "Count": 1,
            "Users": [
                user_id
            ]
        })

        else: #the key exists so just increment the value
            count = message_ref.child(reaction).child("Count").get()
            users = message_ref.child(reaction).child("Users").get()
            #check if user is in the list, else throw an exception:
            if( user_id in users ):
                FireBaseDatabase.closeConnection()
                raise Exception("You have already made that reaction")
            users.append(user_id)
            message_ref.child(reaction).child("Count").set(count+1)
            message_ref.child(reaction).child("Users").set(users)

    FireBaseDatabase.closeConnection()