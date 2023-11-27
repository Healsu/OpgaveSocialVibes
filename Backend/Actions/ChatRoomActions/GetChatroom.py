from Database import FireStore, Querys


def getDataAndMessages(chatroom_id):
    db = FireStore.getConnection()
    chatroom_ref = db.child(f"Chatrooms/{chatroom_id}")
    chatroom_participants_ref = db.child(f"Chatroom Participants/{chatroom_id}") 
    chatroom_messages_ref = db.child(f"Chatroom Messages/{chatroom_id}")


    chatroom_data = chatroom_ref.get()
    chatroom_participants_data = chatroom_participants_ref.get()
    try:
        chatroom_messages_ref.get()
        chatroom_messages_data = chatroom_messages_ref.get()
        return {"Chatroom":chatroom_data, "Participants":chatroom_participants_data, "Messages":chatroom_messages_data}
    except Exception as e:
        print(f"There is no chatroom {e}")
    finally:
        FireStore.closeConnection()
    
    
