from flask import Flask, request, jsonify
from Controller.ProfileController import profile
from Controller.ChatRoomController import chatRoom
from Controller.MessageController import message

app = Flask(__name__)

app.register_blueprint(profile, url_prefix='/profile')
app.register_blueprint(chatRoom, url_prefix='/chatroom')
app.register_blueprint(message, url_prefix='/message')

if __name__ == "__main__":
    app.run(debug=True)