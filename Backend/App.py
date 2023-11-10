from flask import Flask, request, jsonify
from Controller.ProfileController import profile
from Controller.ChatRoomController import chatRoom

app = Flask(__name__)

app.register_blueprint(profile, url_prefix='/profile')
app.register_blueprint(chatRoom, url_prefix='/chatroom')

if __name__ == "__main__":
    app.run(debug=True)