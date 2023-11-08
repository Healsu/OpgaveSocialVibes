from flask import Flask, request, jsonify, render_template, Blueprint
from Actions import SaveProfileDataAction, AddFriendToProfileAction

profile = Blueprint('profile', __name__)#blueprint is mini flask applications that is driven by the main application

@profile.route("/create", methods=["POST"])
def create():
    try:
        user_data = request.get_json()
        print(user_data)
        SaveProfileDataAction.saveProfile(user_data)
        return jsonify({'message': 'Profile created successfully', 'data': user_data}), 200
    except:
        return jsonify({'error': 'Failed to create a profile'}), 500

@profile.route("/<user_id>/add-friend", methods=["PUT"])
def addFriend(user_id):
    try:
        friend_id = request.get_json().get("FriendID")
        print("you tried accessing Doc with id: ", user_id, " and post the body", friend_id)
        AddFriendToProfileAction.saveFriend(str(user_id), str(friend_id))
        


        return jsonify({'message': 'Friend added successfully', 'data': friend_id}), 200
    except:
        return jsonify({'error': 'Failed to add a friend'}), 500