from Database import FireBaseDatabase, Querys

def leave(Event_Id, user_id):
    db = FireBaseDatabase.getConnection()
    
    event_participants_ref = db.child(f"Event Participants/{Event_Id}")

    participants_data = event_participants_ref.get()

    user_profile = Querys.getById(db, "Profiles", user_id)
    
    if user_profile in participants_data:
        participants_data.remove(user_profile)
    else:
        raise Exception("That user is not in the chatroom")
    event_participants_ref.set(participants_data)

    FireBaseDatabase.closeConnection()