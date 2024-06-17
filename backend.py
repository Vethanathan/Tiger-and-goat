from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from Boards import Board
from Games import Game

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

# Queue to manage pending users
pending_users = []

# Dictionary to store active games
active_games = {}

# Dictionary to store user roles and rooms
user_roles = {}
user_rooms = {}

def assign_roles(user1, user2):
    game = Game(user1, user2, Board())
    room = game.room

    user1_role = {"role": "tiger", "message": "You are the tiger!", "room": room}
    user2_role = {"role": "goat", "message": "You are the goat!", "room": room}

    # Join both users to the same room
    join_room(room, user1)
    join_room(room, user2)

    # Send roles to the users
    socketio.emit('role', user1_role, room=user1)
    socketio.emit('role', user2_role, room=user2)

    # Store the roles and rooms in the dictionaries
    user_roles[user1] = "tiger"
    user_roles[user2] = "goat"
    user_rooms[user1] = room
    user_rooms[user2] = room

    # Store the game in the active games list
    active_games[room] = game
    print(active_games)

# Function to handle each WebSocket connection
@socketio.on('connect')
def handle_connect():
    global pending_users

    # Add the new user to the pending users queue
    pending_users.append(request.sid)

    # If this is the first user in the queue, notify them they are waiting for an opponent
    if len(pending_users) == 1:
        emit('message', {"message": "Waiting for an opponent..."})
    # If there are at least two pending users, start a new game
    elif len(pending_users) >= 2:
        user1 = pending_users.pop(0)
        user2 = pending_users.pop(0)
        assign_roles(user1, user2)

@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    if sid in user_roles:
        del user_roles[sid]
    if sid in user_rooms:
        room = user_rooms[sid]
        leave_room(room, sid)
        del user_rooms[sid]
        if room in active_games:
            del active_games[room]
    print(f"Connection closed for {sid}")

@socketio.on('message')
def handle_message(data):
    print(f"Received data: {data}")
    sid = request.sid
    role = user_roles.get(sid, "unknown")
    room = data.get('room')
    message = data.get('message')
    if room:
        curr_game = active_games[room]
        try:
            print(message)
            from_, to_ = message.split(',')
            from_ind, to_ind = Board.board_vals[from_], Board.board_vals[to_]
            curr_game.board.make_move(from_ind, to_ind, role)
            print("test")
            curr_game.board.is_Tiger_turn = not curr_game.board.is_Tiger_turn
            curr_game.board.print_board()

            # Check if the game is over
            game_over, winner = curr_game.board.is_game_over()
            if game_over:
                print(curr_game.board.is_game_over())
                emit('game_over', {"winner": winner}, room=room)
            
            d = {i: None for i in range(23)}

            c=0
            curr_b  =curr_game.board.get_board_state()
            for i in curr_b:
                for j in i:
                    if j=='#':
                        continue
                    if j=='T' or j=='G':
                        d[c]='piece'
                    c+=1   
            print(d)

            # Emit the updated board to all users in the room
            emit('update_board', {"board": d}, room=room)

            print(curr_game.board.goat, curr_game.board.tiger, curr_game.board.killed_goat)
            print(f"Game logic processing: {message}")
        except Exception as e:
            print(f"Error processing move: {e}")
            d = {i: None for i in range(23)}

            c=0
            curr_b  =curr_game.board.get_board_state()
            print(curr_b)
            for i in curr_b:
                for j in i:
                    if j=='#':
                        continue
                    if j=='T' or j=='G':
                        d[c]='piece'
                    c+=1   
            print(d)
            emit('update_board', {"board": d}, room=room)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8765, debug=True)
