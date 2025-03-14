from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database for users and emergency contacts
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users[data['username']] = {
        'password': data['password'],
        'emergency_contacts': data['emergency_contacts']
    }
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/emergency', methods=['POST'])
def emergency():
    data = request.json
    user = users.get(data['username'])
    if user:
        # Here, you would send an alert to the user's emergency contacts
        return jsonify({'message': 'Emergency alert sent'}), 200
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
