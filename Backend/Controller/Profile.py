from flask import Flask, request, jsonify, render_template, Blueprint
from Actions import SaveProfileDataAction

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

@profile.route("<user_id>/add-friend", methods=["POST"])
def addFriend():
    try:
        



        return jsonify({'message': 'Friend added successfully', 'data': user_data}), 200
    except:
        return jsonify({'error': 'Failed to add a friend'}), 500