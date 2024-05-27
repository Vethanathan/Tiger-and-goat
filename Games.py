# class Game():
#     def __init__(self,player1,player2,state,moves,start_time):
#         self.player1 = player1
#         self.player2 = player2
#         self.state = state 
#         self.noves =moves 
#         self.start_time = start_time

import uuid
class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.room = f"room_{uuid.uuid4()}"
        self.roles = {"tiger": player1, "goat": player2}

    def get_role(self, player):
        for role, p in self.roles.items():
            if p == player:
                return role
        return None