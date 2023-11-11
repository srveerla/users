from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/library"
mongo = PyMongo(app)

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

@app.route('/users', methods=['GET'])
def get_users():
    users = list(mongo.db.users.find({}, {'_id': 0}))
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = User(data['username'], data['email'])
    mongo.db.users.insert_one(user.__dict__)
    return 'User added', 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
