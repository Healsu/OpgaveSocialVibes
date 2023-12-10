from .Extensions import socketio, emit, join_room, leave_room
from Actions.ChatRoomActions import GetChatroomMessages

@socketio.on('chatroom_join')
def handle_chatroom(data):
    print("User Opened the chatroom")

    chatroom_id = data['chatroom_id']

    join_room(chatroom_id)
    user_data = GetChatroomMessages.getMessages(chatroom_id)
    messages = []
    for key in user_data:
        messages.append(user_data[key])
        
    emit('message_list', messages, broadcast=True, room=chatroom_id)

@socketio.on('chatroom_leave')
def handle_leave_chatroom(data):
    print("User Closed the chatroom")

    chatroom_id = data['chatroom_id']
    
    leave_room(chatroom_id)