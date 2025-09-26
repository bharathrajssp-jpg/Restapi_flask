from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple list to store users
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

# GET - Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET - Get single user
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST - Create user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_id = max([u['id'] for u in users]) + 1 if users else 1
    new_user = {
        "id": new_id,
        "name": data['name'],
        "email": data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT - Update user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user)

# DELETE - Delete user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    user = next((u for u in users if u['id'] == id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users = [u for u in users if u['id'] != id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)