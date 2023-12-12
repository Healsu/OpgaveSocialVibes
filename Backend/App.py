from flask import Flask
from Controller.ProfileController import profile
from Controller.ChatRoomController import chatRoom
from Controller.MessageController import message
from WebSocket.MessageEvents import socketio
from Controller.CommunityController import community
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'secret!'

    CORS(app, origins=["http://localhost:8100/*"])

    app.register_blueprint(profile, url_prefix='/profile')
    app.register_blueprint(chatRoom, url_prefix='/chatroom')
    app.register_blueprint(message, url_prefix='/message')
    app.register_blueprint(community, url_prefix="/community")

    socketio.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    socketio.run(app, host='127.0.0.1', port=5000)
