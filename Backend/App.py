from flask import Flask, request, jsonify
from Controller.Profile import profile

app = Flask(__name__)

app.register_blueprint(profile, url_prefix='/profile')
 
if __name__ == "__main__":
    app.run(debug=True)