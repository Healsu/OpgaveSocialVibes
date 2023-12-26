from flask import request, jsonify, Blueprint, send_file
from Actions.ChatRoomActions import CreateChatRoomAction, DeleteChatRoomAction, AddUserToChatroomAction, LeaveChatRoomAction, GetChatroomMessages, GetChatroomWithUserAction, GetChatroom
import json
chatRoom = Blueprint('chatRoom', __name__)


@chatRoom.route("/create-chat", methods=["POST"])
def createChatroom():
    try:
        request_body = request.get_json()

        chatRoomID, chatRoomType = CreateChatRoomAction.craeteChatroom(request_body)
        return jsonify({'message': 'Chatroom created successfully', "chatroomID":chatRoomID, "chatroomType":chatRoomType}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'Chatroom creation failed', 'data': request_body}), 500
    

@chatRoom.route("/delete-chat/<chatroom_id>", methods=["DELETE"])
def deleteChatroom(chatroom_id):
    try:
        DeleteChatRoomAction.deleteChatroom(chatroom_id)

        return jsonify({'message': 'Chatroom deleted'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Could not delete chatroom'}), 500


@chatRoom.route("/join-chatroom/<chatroom_id>", methods=["PATCH"])
def addUserToChatroom(chatroom_id):
    try:
        user_id = request.get_json().get("user_Id")
        
        AddUserToChatroomAction.addUser(str(chatroom_id), str(user_id))

        return jsonify({'message': 'User added to chatroom'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Could not add user to chatroom'}), 500


@chatRoom.route("/leave-chatroom/<chatroom_id>", methods=["PATCH"])
def removeUserFromChatroom(chatroom_id):
    try:
        user_id = request.get_json().get("user_Id")

        LeaveChatRoomAction.leave(str(chatroom_id), str(user_id))

        return jsonify({'message': 'User left the chatroom'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'User could not leave the chatroom'}), 500
    
@chatRoom.route("/user-get/<user_id>")
def getUserChatrooms(user_id):
    try:
        chatroom_data = GetChatroomWithUserAction.userInChatroom(str(user_id))

        return jsonify({'message': 'Chatroom retrieved', 'chatrooms': chatroom_data}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'There is no chatroom with that id'}), 500

@chatRoom.route("/get/<chatroom_id>")
def getChatroom(chatroom_id):
    try:
        chatroom_data = GetChatroom.getData(str(chatroom_id))

        return jsonify({'message': 'Chatroom retrieved', 'chatroom_data': chatroom_data}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'There is no chatroom with that id'}), 500
    
@chatRoom.route("/get-messages/<chatroom_id>")
def getChatroomMessages(chatroom_id):
    try:
        chatroom_data = GetChatroomMessages.getMessages(str(chatroom_id))

        return jsonify({'message': 'Chatroom Messages retrieved', 'messages': chatroom_data}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'There is no chatroom with that id'}), 500


#VERIFY ALL API's THAT THEY ARE AN TYPE OF CHATROOM LIKE WE DO IN COMMUNITY.