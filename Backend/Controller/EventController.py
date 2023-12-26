from flask import request, jsonify, Blueprint
from Actions.EventActions import CreateEventAction, GetEventAction, JoinEventAction, LeaveEventAction, GetUserEventsAction

event = Blueprint('event', __name__)


@event.route("/create-event", methods=["POST"])
def Create():
    try:
        request_body = request.get_json()

        CreateEventAction.create(request_body)
        
        return jsonify({'message': 'Event created successfully'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'Event creation failed'}), 500
    
@event.route("/get/<Event_Id>")
def Get(Event_Id):
    try:
        data = GetEventAction.Get(str(Event_Id))

        return jsonify({"message": "Event retrieved", "Data": data}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'Event retrieved failed'}), 500

@event.route("/get-all")
def GetAll():
    try:
        data = GetEventAction.GetAll()

        return jsonify({"message": "Events retrieved", "Data": data}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'Events retrieved failed'}), 500
    
@event.route("/join/<Event_Id>", methods=["PATCH"])
def join(Event_Id):
    try:
        user_id = request.get_json().get("user_Id")

        JoinEventAction.join(str(Event_Id), str(user_id))

        return jsonify({"message": "Event joined"}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': f'Event join failed: {e}'}), 500
    
@event.route("/leave/<Event_Id>", methods=["PATCH"])
def leave(Event_Id):
    try:
        user_id = request.get_json().get("user_Id")

        LeaveEventAction.leave(str(Event_Id), str(user_id))

        return jsonify({'message': 'User left the Event'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'User could not leave the Event'}), 500

@event.route("user-events/<User_ID>")
def userGet(User_ID):
    try:
        data = GetUserEventsAction.get(User_ID)
        
        return jsonify({"message": "Event retrieved", "Data": data}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'Event retrieved failed'}), 500