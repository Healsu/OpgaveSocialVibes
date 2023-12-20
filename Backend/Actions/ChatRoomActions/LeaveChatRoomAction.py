from Database import FireBaseDatabase, Querys

def leave(chatroom_id, user_id):
    db = FireBaseDatabase.getConnection()
    
    chatroom_participants_ref = db.child(f"Chatroom Participants/{chatroom_id}")

    participants_data = chatroom_participants_ref.get()

    user_profile = Querys.getById(db, "Profiles", user_id)
    if user_profile in participants_data:
        participants_data.remove(user_profile)
    else:
        raise Exception("That user is not in the chatroom")
    chatroom_participants_ref.set(participants_data)

    FireBaseDatabase.closeConnection()