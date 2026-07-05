\# NetChat — Real-time Chat Application



A real-time group chat web app built with Flask-SocketIO, demonstrating WebSocket-based bidirectional communication (Networking course project).



\## Features

\- Real-time messaging between multiple users — no page refresh needed

\- Join notifications when a user enters the chat

\- Own messages styled differently from others' messages

\- Message timestamps



\## How It Works (Networking Concepts)

\- Uses \*\*WebSocket\*\* protocol instead of traditional HTTP request-response

\- Server maintains a persistent connection with every client

\- Messages are \*\*broadcast\*\* by the server to all connected clients instantly



\## Tech Stack

\- Python (Flask, Flask-SocketIO)

\- JavaScript (Socket.IO client)

\- HTML, CSS



\## How to Run

1\. Install: `pip install flask flask-socketio`

2\. Run: `python app.py`

3\. Open \*\*two browser tabs\*\* at `http://127.0.0.1:5000` and chat between them!



\## Author

Naymur Rahman — CSE, Notre Dame University Bangladesh

