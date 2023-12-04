from flask import request, jsonify, Blueprint
from Actions.MessageActions import SendMessageAction, DeleteMessageAction

message = Blueprint('message', __name__)


@message.route("/send-message/<chatroom_id>", methods=["POST"])
def sendMessage(chatroom_id):
    try:
        message = request.form.get("message")
        senderId = request.form.get("senderID")
        message_image = request.files.get("image")
        SendMessageAction.SendMessage(chatroom_id, message, senderId, message_image)

        return jsonify({'message': 'Message sent'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Message could not be sent'}), 500


@message.route("/delete-message/<chatroom_id>", methods=["DELETE"])
def deleteMessage(chatroom_id):
    try:
        #get the chatroom id
        message_id = request.get_json().get("message_id")

        DeleteMessageAction.deleteMessage(str(message_id), str(chatroom_id))
        return jsonify({'message': 'Deletion completed'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Message could not be deleted'}), 500
