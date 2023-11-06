from flask import Flask, request, jsonify, render_template

profile = Flask(__name__)

@profile.route("/add-friend/<user_id>")
def addFriend(user_id):
    return "hello World", 202

@profile.route("/create-profile", methods=["POST"])
def createProfile(user_data):
    user_data = request.args.get("user_id")