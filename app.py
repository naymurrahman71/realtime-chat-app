from flask import Flask
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.secret_key = "chat-secret-2026"
socketio = SocketIO(app)

PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>NetChat</title>
<style>
    body { font-family: Arial, sans-serif; background: #0f172a; margin: 0;
           display: flex; flex-direction: column; height: 100vh; }
    .header { background: #7c3aed; color: white; padding: 15px; text-align: center; }
    .header h2 { margin: 0; }
    #chat { flex: 1; overflow-y: auto; padding: 20px; }
    .msg { background: #1e293b; color: #e2e8f0; padding: 10px 15px;
           border-radius: 10px; margin-bottom: 10px; max-width: 70%; }
    .msg .who { color: #a78bfa; font-weight: bold; }
    .msg .time { color: #64748b; font-size: 11px; margin-left: 8px; }
    .mine { background: #7c3aed; color: white; margin-left: auto; }
    .mine .who { color: #ddd6fe; }
    .sys { color: #64748b; text-align: center; font-size: 13px; margin: 8px 0; }
    #bottom { display: flex; padding: 15px; background: #1e293b; gap: 10px; }
    input { flex: 1; padding: 12px; border: none; border-radius: 8px;
            background: #334155; color: white; font-size: 15px; }
    input::placeholder { color: #94a3b8; }
    button { background: #7c3aed; color: white; border: none;
             padding: 12px 25px; border-radius: 8px; cursor: pointer; font-size: 15px; }
    button:hover { background: #6d28d9; }
</style>
</head>
<body>
    <div class="header"><h2>💬 NetChat — Real-time Chat</h2></div>
    <div id="chat"></div>
    <div id="bottom">
        <input id="message" placeholder="Type a message..." autocomplete="off">
        <button onclick="send()">Send</button>
    </div>

<script src="https://cdn.socket.io/4.7.5/socket.io.min.js"></script>
<script>
    const socket = io();
    let username = prompt("আপনার নাম লিখুন:") || "Anonymous";
    socket.emit("joined", {user: username});

    function send() {
        const box = document.getElementById("message");
        if (box.value.trim() === "") return;
        socket.emit("send_message", {user: username, text: box.value});
        box.value = "";
        box.focus();
    }

    document.getElementById("message").addEventListener("keydown", e => {
        if (e.key === "Enter") send();
    });

    socket.on("new_message", data => {
        const chat = document.getElementById("chat");
        const div = document.createElement("div");
        div.className = data.user === username ? "msg mine" : "msg";
        div.innerHTML = `<span class="who">${data.user}</span>` +
                        `<span class="time">${data.time}</span><br>${data.text}`;
        chat.appendChild(div);
        chat.scrollTop = chat.scrollHeight;
    });

    socket.on("user_joined", data => {
        const chat = document.getElementById("chat");
        const div = document.createElement("div");
        div.className = "sys";
        div.textContent = `👋 ${data.user} joined the chat`;
        chat.appendChild(div);
        chat.scrollTop = chat.scrollHeight;
    });
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return PAGE

@socketio.on("joined")
def handle_join(data):
    emit("user_joined", {"user": data["user"]}, broadcast=True)

@socketio.on("send_message")
def handle_message(data):
    emit("new_message", {
        "user": data["user"],
        "text": data["text"],
        "time": datetime.now().strftime("%H:%M")
    }, broadcast=True)

socketio.run(app, debug=True)