from flask import request, jsonify, Blueprint
from Actions.ProfileActions import CreateProfileAction, GetProfileDataAction, GetFriendsListAction, GetPaginatedProfilesAction, GetAllProfiles

profile = Blueprint('profile', __name__)#blueprint is mini flask applications that is driven by the main application

@profile.route("/create", methods=["POST"])
def create():
    try:
        user_data = request.get_json()

        CreateProfileAction.saveProfile(user_data)
        
        return jsonify({'message': 'Profile created successfully', 'data': user_data}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Failed to create a profile'}), 500


@profile.route("/get/<user_id>")
def getProfile(user_id):
    try:
        profile_data =  GetProfileDataAction.getProfile(str(user_id))

        return jsonify({'message': 'Profile Retrieved', 'data': profile_data}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'No profile with that id found'}), 500


@profile.route("/get-friends/<user_id>")
def getFriends(user_id):
    try:
        friend_list =  GetFriendsListAction.getFriends(str(user_id))

        return jsonify({'message': 'Profile friends Retrieved', 'data': friend_list}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'That profile has no friends'}), 500
    
@profile.route("/pagination-get/<start_number>")
def getPaginatedProfiles(start_number):
    try:
        profiles = GetPaginatedProfilesAction.GetFromIndex(start_number)

        return jsonify({'message': 'Profile friends Retrieved', 'profiles': profiles}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'That profile has no friends'}), 500

@profile.route("/get-all-profiles")
def getAllProfiles():
    try:
        profiles = GetAllProfiles.get()

        return jsonify({'message': 'Profile friends Retrieved', 'profiles': profiles}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'That profile has no friends'}), 500