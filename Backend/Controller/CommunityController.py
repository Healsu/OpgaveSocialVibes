from flask import request, jsonify, Blueprint, send_file
from Actions.CommunityActions import CreateCommunityAction, VerifyIsCommunityChatroomAction, GetCommunityWhitoutUserAction, BanUserFromCommunityAction
from Actions.ChatRoomActions import AddUserToChatroomAction, LeaveChatRoomAction

community = Blueprint('community', __name__)


@community.route("create-community", methods=["POST"])
def create():
    try:
        request_body = request.get_json()
        print(request_body)
        CreateCommunityAction.createCommunity(request_body)

        return jsonify({'message': 'Community created successfully'}), 200
    except Exception as e:
        return jsonify({'message': f'Community creation failed: {e}'}), 500
    
@community.route("join-community/<chatroom_id>", methods=["POST"])
def join(chatroom_id):
    try:
        #verify that the chatroom is actually of the type community
        isCommunity = VerifyIsCommunityChatroomAction.IsCommunity(chatroom_id)
        if(isCommunity is False):
            raise Exception("This is not an community")

        #add the user to the communityParticipantsArray in the database.
        user_id = request.get_json().get("user_Id")

        AddUserToChatroomAction.addUser(chatroom_id, user_id)

        return jsonify({'message': 'Community joined successfully'}), 200
    except Exception as e:
        return jsonify({'message': f'Community joined failed: {e}'}), 500
    

@community.route("leave-community/<chatroom_id>", methods=["POST"])
def leave(chatroom_id):
    try:
        #verify that the chatroom is actually of the type community
        isCommunity = VerifyIsCommunityChatroomAction.IsCommunity(chatroom_id)
        if(isCommunity is False):
            raise Exception("This is not an community")
        
        #add the user to the communityParticipantsArray in the database.
        user_id = request.get_json().get("user_Id")

        LeaveChatRoomAction.leave(chatroom_id, user_id)

        return jsonify({'message': 'Community quit successfully'}), 200
    except Exception as e:
        return jsonify({'message': f'Community quit failed: {e}'}), 500


@community.route("get-all-communitys/<user_id>")
def get(user_id):
    try:

        data = GetCommunityWhitoutUserAction.get(user_id)

        return jsonify({'message': 'Community retrieved successfully', "Chatrooms": data}), 200
    except Exception as e:
        return jsonify({'message': f'Community retrieved failed: {e}'}), 500


@community.route("Ban-user/<Community_id>", methods=["POST"])
def ban(Community_id):
    isCommunity = VerifyIsCommunityChatroomAction.IsCommunity(Community_id)
    user_id = request.get_json().get("user_Id")

    if(isCommunity is False):
        raise Exception("This is not an community")
    
    

    BanUserFromCommunityAction.ban()