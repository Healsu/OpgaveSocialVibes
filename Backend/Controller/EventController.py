from flask import request, jsonify, Blueprint
from Actions.EventActions import CreateEventAction, GetEventAction

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
    
@event.route("/join/<Event_Id>", methods=["POST"])
def join(Event_Id):
    pass