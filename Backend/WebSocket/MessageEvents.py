from .Extensions import socketio, emit, join_room, leave_room
from Actions.ChatRoomActions import GetChatroomMessages
from Database import FireBaseDatabase, Querys


@socketio.on('chatroom_join')
def handle_chatroom(data):
    print("User Opened the chatroom")

    chatroom_id = data['chatroom_id']
    user_id = data.get('user_id', None)

    #check if the chatroom is a community and then if the user is banned


    join_room(chatroom_id, user_id)
    user_data = GetChatroomMessages.getMessages(chatroom_id)
    messages = []
    for key in user_data:
        messages.append(user_data[key])
        
    emit('message_list', messages, broadcast=True, room=chatroom_id)

@socketio.on('chatroom_leave')
def handle_leave_chatroom(data):
    print("User Closed the chatroom")
    chatroom_id = data['chatroom_id']
    user_id = data.get('user_id', None)

    leave_room(chatroom_id, user_id)

@socketio.on('banned')
def handle_banned_user(data):
    print("Banning user and reomving them from the room")
    user_id = data.get('user_id', None)
    chatroom_id = data['chatroom_id']

    #Check if the user exist:
    db = FireBaseDatabase.getConnection()
    profile_to_ban = Querys.getById(db, "Profiles", user_id)
    if profile_to_ban == None:
        emit("Banned_Fail", False, broadcast=True, room=chatroom_id)#emit that the user can't be banned to the chatroom
        
        #Add the user to a banned list in the database



    else:
        leave_room(chatroom_id, user_id)
    FireBaseDatabase.closeConnection()
    print("User has been removed from the room")