from Database import FireBaseDatabase, FireBaseStorage


def getData(chatroom_id):
    try:
        # retrieve the data
        db = FireBaseDatabase.getConnection()
        chatroom_ref = db.child(f"Chatrooms/{chatroom_id}")
        chatroom_participants_ref = db.child(f"Chatroom Participants/{chatroom_id}") 
        

        chatroom_data = chatroom_ref.get()
        chatroom_id = chatroom_ref.key
        chatroom_participants_data = chatroom_participants_ref.get()

        FireBaseDatabase.closeConnection()
        print({"Chatroom":chatroom_data, "Participants":chatroom_participants_data})
        return {"Chatroom":chatroom_data, "Participants":chatroom_participants_data, "Chatroom Id": chatroom_id}
    except Exception as e:
        raise Exception(f"Something went wrong: {e}")