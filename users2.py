from flask import Flask, request, jsonify

app = Flask(__name__)

# Users database
users = {}

# Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.get_json()
    username = user_data["username"]
    password = user_data["password"]

    users[username] = password

    return jsonify({
        "success": True,
        "message": "User created successfully."
    })

# Get all users
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify({
        "success": True,
        "users": users
    })

# Get a specific user
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username not in users:
        return jsonify({
            "success": False,
            "message": "User does not exist."
        })

    return jsonify({
        "success": True,
        "user": {
            "username": username,
            "password": users[username]
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
