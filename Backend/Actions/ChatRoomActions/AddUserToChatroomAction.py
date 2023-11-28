from Database import FireBaseDatabase, Querys
from google.cloud import firestore

def addUser(chatroom_id, user_id):
    db = FireBaseDatabase.getConnection()
    
    chatroom_participants_ref = db.child(f"Chatroom Participants/{chatroom_id}")

    participants_data = chatroom_participants_ref.get()

    user_profile = Querys.getById(db, "Profiles", user_id)
    if user_profile not in participants_data:
        participants_data.append(user_profile)
    else:
        FireBaseDatabase.closeConnection()
        raise Exception("That user is already in the chatroom")
    chatroom_participants_ref.set(participants_data)

    FireBaseDatabase.closeConnection()

        

    

    