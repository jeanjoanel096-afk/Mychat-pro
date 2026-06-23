from flask import Flask, render_template, request, jsonify, session
from flask_socketio import SocketIO, emit, join_room
import firebase_admin
from firebase_admin import credentials, firestore, auth

# 1. Konfigirasyon
app = Flask(__name__)
app.secret_key = 'mychat_secret_key_2026'
socketio = SocketIO(app, cors_allowed_origins="*")

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 2. ROUTES (Paj yo)
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# 3. EARNINGS SYSTEM (API)
@app.route('/add_points', methods=['POST'])
def add_points():
    data = request.json
    uid = data.get('uid')
    # Update Firestore
    db.collection('users').document(uid).update({
        'points': firestore.Increment(25),
        'videos_watched': firestore.Increment(1)
    })
    return jsonify({"success": True})

# 4. CHAT SYSTEM (SocketIO)
@socketio.on('send_message')
def handle_message(data):
    # Sove nan Firestore
    db.collection("chats").add({
        "sender": data['sender'],
        "text": data['message'],
        "timestamp": firestore.SERVER_TIMESTAMP
    })
    # Voye bay lòt moun
    emit('receive_message', data, broadcast=True)

# 5. WITHDRAWAL SYSTEM
@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    uid = data.get('uid')
    amount = data.get('amount')
    # Lojik pou retrè a
    db.collection('withdrawals').add({
        'uid': uid,
        'amount': amount,
        'status': 'pending',@app.route('/chat')
def chat():
    return render_template('chat.html')
        'method': 'MonCash'
    })
    return jsonify({"status": "demann voye"})@app.route('/signup')@app.route('/profile')
def profile():
    return render_template('profile.html')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
