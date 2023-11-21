from flask import request, jsonify, Blueprint
from Actions.MessageActions import SendMessageAction, DeleteMessageAction

message = Blueprint('message', __name__)


@message.route("/<chatroom_id>/send-message", methods=["POST"])
def sendMessage(chatroom_id):
    try:
        message = request.get_json().get("message")
        senderId = request.get_json().get("senderID")
        SendMessageAction.SendMessage(chatroom_id, message, senderId)

        return jsonify({'message': 'Message sent'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Message could not be sent'}), 500


@message.route("/<chatroom_id>/delete-message", methods=["DELETE"])
def deleteMessage(chatroom_id):
    try:
        #get the chatroom id
        message_id = request.get_json().get("message_id")

        DeleteMessageAction.deleteMessage(str(message_id), str(chatroom_id))
        return jsonify({'message': 'Deletion completed'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Message could not be deleted'}), 500
