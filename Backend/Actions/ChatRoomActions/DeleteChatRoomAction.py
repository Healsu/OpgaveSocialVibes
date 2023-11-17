from Database import FireStore, Querys
from google.cloud.exceptions import NotFound

def deleteChatroom(chatroom_id):
    db = FireStore.getConnection()
    
    chatroom_ref = db.child("Chatrooms").child(chatroom_id)
    

    #checks if any deletion has occurred
    is_deleted = False

    if chatroom_ref.get():
        chatroom_ref.delete()
        is_deleted = True
    else:
        print("There is no chatroom by that id")

    chatroom_participants_ref = db.child("Chatroom Participants").child(chatroom_id)
    
    if chatroom_participants_ref.get():
        chatroom_participants_ref.delete()
        is_deleted = True
    else:
        print("There is no chatroom Participants by that id")
    
    chatroom_messeges_ref = db.child("Chatrooms Messages").child(chatroom_id)
    
    if chatroom_messeges_ref.get():
        chatroom_messeges_ref.delete()
        is_deleted = True
    else:
        print("There is no chatroom Messages by that id")
    
    if not is_deleted:
        raise ValueError("No deletion operation was performed. Chatroom not found.")
    
    FireStore.closeConnection()