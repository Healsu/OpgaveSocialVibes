from Database import FireBaseDatabase, Querys


def join(Event_Id, user_id):
    db = FireBaseDatabase.getConnection()

    event_participants_ref = db.child(f"Event Participants/{Event_Id}")

    participants_data = event_participants_ref.get()
    print(participants_data)
    user_profile = Querys.getById(db, "Profiles", user_id)
    if user_profile not in participants_data:
        participants_data.append(user_profile)
    else:
        FireBaseDatabase.closeConnection()
        raise Exception("That user is already in the chatroom")
    event_participants_ref.set(participants_data)
    
    FireBaseDatabase.closeConnection()