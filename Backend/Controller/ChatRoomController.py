from flask import request, jsonify, Blueprint
from Actions.ChatRoomActions import CreateChatRoomAction, DeleteChatRoomAction, AddUserToChatroomAction, LeaveChatRoomAction, GetChatroom, GetChatroomWithUserAction

chatRoom = Blueprint('chatRoom', __name__)


@chatRoom.route("/create-chat", methods=["POST"])
def createChatroom():
    try:
        request_body = request.get_json()

        CreateChatRoomAction.craeteChatroom(request_body)
        return jsonify({'message': 'Chatroom created successfully', 'data': request_body}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'Chatroom creation failed', 'data': request_body}), 500
    

@chatRoom.route("/<chatroom_id>/delete-chat", methods=["DELETE"])
def deleteChatroom(chatroom_id):
    try:
        DeleteChatRoomAction.deleteChatroom(chatroom_id)

        return jsonify({'message': 'Chatroom deleted'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Could not delete chatroom'}), 500


@chatRoom.route("/<chatroom_id>/join-chatroom", methods=["PATCH"])
def addUserToChatroom(chatroom_id):
    try:
        user_id = request.get_json().get("user_Id")
        
        AddUserToChatroomAction.addUser(str(chatroom_id), str(user_id))

        return jsonify({'message': 'User added to chatroom'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Could not add user to chatroom'}), 500


@chatRoom.route("/<chatroom_id>/leave-chatroom", methods=["PATCH"])
def removeUserFromChatroom(chatroom_id):
    try:
        user_id = request.get_json().get("user_Id")

        LeaveChatRoomAction.leave(str(chatroom_id), str(user_id))

        return jsonify({'message': 'User left the chatroom'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'User could not leave the chatroom'}), 500


@chatRoom.route("/<chatroom_id>/get")
def getChatroom(chatroom_id):
    try:
        chatroom_data = GetChatroom.getDataAndMessages(str(chatroom_id))

        return jsonify({'message': 'Chatroom retrieved', 'chatroom_data': chatroom_data}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'There is no chatroom with that id'}), 500
    
@chatRoom.route("/<user_id>/user-get")
def getUserChatrooms(user_id):
    try:
        chatroom_data = GetChatroomWithUserAction.userInChatroom(str(user_id))
        return jsonify({'message': 'Chatroom retrieved', 'chatroom_ids': chatroom_data}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'There is no chatroom with that id'}), 500

@chatRoom.route("/<chatroom_id>/get-messages")
def getChatroomMessages(chatroom_id):
    try:
        chatroom_data = GetChatroom.getDataAndMessages(str(chatroom_id))
        return jsonify({'message': 'Chatroom retrieved', 'chatroom_messages': chatroom_data["Messages"]}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'There is no chatroom with that id'}), 500
#Add delete chat messages to delete chatroom