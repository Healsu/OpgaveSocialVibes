from Database import FireStore, Querys

def leave(chatroom_id, user_id):
    db = FireStore.getConnection()
    
    chatroom_participants_ref = db.child(f"Chatroom Participants/{chatroom_id}")

    participants_data = chatroom_participants_ref.get()

    user_profile = Querys.getById(db, "Profiles", user_id)
    if user_profile in participants_data:
        participants_data.remove(user_profile)
    else:
        raise Exception("That user is already in the chatroom")
    chatroom_participants_ref.set(participants_data)



    FireStore.closeConnection()