from .Extensions import socketio, emit, join_room, leave_room
from Actions.ChatRoomActions import GetChatroom

@socketio.on("message")
def handle_connect(message):
    emit("message", message, broadcast=True)


@socketio.on('chatroom_join')
def handle_chatroom(data):
    print("User joined the chatroom")

    chatroom_id = data['chatroom_id']

    join_room(chatroom_id)
    print(chatroom_id)
    user_data = GetChatroom.getDataAndMessages(chatroom_id)
    
    emit('message_list', user_data['Messages'], broadcast=True)

    # Perform any other actions based on the received data
