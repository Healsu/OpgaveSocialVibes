from Database import FireBaseDatabase

def IsCommunity(chatroom_id):
    db = FireBaseDatabase.getConnection()
    isCommunity = db.child("Chatrooms").child(chatroom_id).child("Type").get()
    FireBaseDatabase.closeConnection()
    return True if isCommunity == "Community" else False

