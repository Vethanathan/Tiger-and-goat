# from Validator import Validator
def find_coordinate_between(index1, index2):
        # Calculate the average of each dimension to find the midpoint
        x_coord = (index1[0] + index2[0]) / 2
        y_coord = (index1[1] + index2[1]) / 2
        if (int(x_coord),int(y_coord))  in (index1,index2):
            return False
        return (int(x_coord), int(y_coord))  # Return as integers


class Board:
    board_vals= {'*':('*','*'),'a': (0, 2), 'b': (1, 0), 'c': (1, 1), 'd': (1, 2), 'e': (1, 3), 'f': (1, 4), 'g': (1, 5), 'h': (2, 0), 'i': (2, 1), 'j': (2, 2), 'k': (2, 3), 'l': (2, 4), 'm': (2, 5), 'n': (3, 0), 'o': (3, 1), 'p': (3, 2), 'q': (3, 3), 'r': (3, 4), 's': (3, 5), 't': (4, 1), 'u': (4, 2), 'v': (4, 3), 'w': (4, 4)}
    invalid_dest=[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (4, 0), (4, 0)]
    

    def __init__(self):

        self.board =[
            ['#','#','_','#','#','#'],
            ['_','_','_','_','_','_'],
            ['_','_','_','_','_','_'],
            ['_','_','_','_','_','_'],
            ['#','_','_','_','_','#']
            ] 
        self.goat = 15
        self.tiger = 3
        self.killed_goat = 0
        self.gameover = False
        self.is_Tiger_turn = True
        self.winner  =  None
        
    def get_board_state(self):
        return self.board
    def print_board(self):
        for i in range(5):
            for j in range(6):
                print(self.board[i][j], end=" ")
            print()
    # def can_any_t_move(self):
    #     rows = len(self.board)
    #     cols = len(self.board[0])
        
    #     def can_move(i, j):
    #         # Check upward move
    #         if i >= 2 and self.board[i - 1][j] == 'G' and self.board[i - 2][j] == '_':
    #             return True
    #         # Check downward move
    #         if i <= rows - 3 and self.board[i + 1][j] == 'G' and self.board[i + 2][j] == '_':
    #             return True
    #         # Check left move
    #         if j >= 2 and self.board[i][j - 1] == 'G' and self.board[i][j - 2] == '_':
    #             return True
    #         # Check right move
    #         if j <= cols - 3 and self.board[i][j + 1] == 'G' and self.board[i][j + 2] == '_':
    #             return True
    #         return False

    #     # Find all 'T' positions and check if any can move
    #     for i in range(rows):
    #         for j in range(cols):
    #             if self.board[i][j] == 'T' and can_move(i, j):
    #                 return True
        
    #     return False

    def can_move(self):
        # Find the position of 'T'
        t_row, t_col = None, None
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'T':
                    t_row, t_col = i, j
                    break
            if t_row is not None:
                break
        
        # Define general possible directions: up, down, left, right
        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]
        
        # Special movement rules for 'T' at (0, 2)
        if (t_row, t_col) == (0, 2):
            special_moves = [
                (1, 1), (1, 2), (1, 3), (1, 4)
            ]
            special_jumps = [
                (2, 1), (2, 2), (2, 3), (2, 4)
            ]
            
            for move in special_moves:
                if 0 <= move[0] < len(self.board) and 0 <= move[1] < len(self.board[0]):
                    if self.board[move[0]][move[1]] == '_':
                        return True
            
            for jump in special_jumps:
                if 0 <= jump[0] < len(self.board) and 0 <= jump[1] < len(self.board[0]):
                    mid_r = (0 + jump[0]) // 2
                    mid_c = (2 + jump[1]) // 2
                    if self.board[mid_r][mid_c] == 'G' and self.board[jump[0]][jump[1]] == '_':
                        return True

        # General movement rules for other positions of 'T'
        for dr, dc in directions:
            new_r, new_c = t_row + dr, t_col + dc
            # Check if the new position is within bounds
            if 0 <= new_r < len(self.board) and 0 <= new_c < len(self.board[0]):
                if self.board[new_r][new_c] == '_':
                    return True  # T can move to an empty cell
                    
                # Check if T can jump over a G
                if self.board[new_r][new_c] == 'G':
                    jump_r, jump_c = new_r + dr, new_c + dc
                    # Check if the jump position is within bounds and empty
                    if 0 <= jump_r < len(self.board) and 0 <= jump_c < len(self.board[0]):
                        if self.board[jump_r][jump_c] == '_':
                            return True  # T can jump over G to an empty cell
        
        return False




    def make_move(self,from_board,to_board,role):
        from_row, from_col = from_board
        to_row, to_col = to_board
        if not self.isvalid_move(from_board,to_board):
            raise Exception("Invalid Move, pls refer the manual")
        else:
            if role == 'tiger' and self.is_Tiger_turn:
                if not from_board == ('*','*') and self.is_Tiger_turn:
                    tup = find_coordinate_between(from_board,to_board)
                if from_board==('*','*'):
                    if self.board[to_row][to_col] == 'G'and self.is_Tiger_turn:
                        raise Exception("Goat is already present")
                    elif self.tiger!=0 and self.board[to_row][to_col]=='_' and self.is_Tiger_turn:
                        self.board[to_row][to_col] = 'T'
                        self.tiger-=1
                        if self.is_game_over()[0]:
                            self.gameover = True
                    elif self.tiger==0 and self.is_Tiger_turn:
                        raise Exception("No tiger present")
                else:
                    if tup:
                        if self.board[from_row][from_col] == 'T' and self.board[tup[0]][tup[1]] == 'G' and self.is_Tiger_turn:
                            # self.goat -= 1
                            self.killed_goat += 1
                            self.board[tup[0]][tup[1]] = '_'
                            self.board[from_row][from_col] = '_'
                            self.board[to_row][to_col] = 'T'
                            if self.is_game_over()[0]:
                                self.gameover = True
                                self.winner = self.is_game_over()[1]

                        else:
                            raise Exception("Tiger cannot jump one position without eating goat")
                    else:
                        if self.board[from_row][from_col] == 'T' and self.board[to_row][to_col] =='_' and self.is_Tiger_turn:
                            self.board[from_row][from_col] = '_'
                            self.board[to_row][to_col] = 'T'
                            if self.is_game_over()[0]:
                                self.gameover = True
            elif role == 'goat':
                if not from_board == ('*','*') and not self.is_Tiger_turn:
                    tup = find_coordinate_between(from_board,to_board)
                if from_board==('*','*') and not self.is_Tiger_turn:
                    if self.board[to_row][to_col] == 'T':
                        raise Exception("Tiger already present")
                    elif self.goat!=0 and self.board[to_row][to_col]=='_' and not self.is_Tiger_turn:
                        self.board[to_row][to_col] = 'G'
                        self.goat-=1
                        if self.is_game_over()[0]:
                            self.gameover = True
                    elif self.goat==0 and not self.is_Tiger_turn:
                        raise Exception("No goat present")

                else:
                    if tup and not self.is_Tiger_turn:
                        raise Exception("Goat cannot eat tiger")
                    else:
                        if self.board[from_row][from_col] == 'G' and self.board[to_row][to_col] =='_' and not self.is_Tiger_turn:
                            self.board[from_row][from_col] = '_'
                            self.board[to_row][to_col] = 'G'
                            if self.is_game_over()[0]:
                                self.gameover = True
                

        
    def board_index(self):
        invalid_dest=[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (4, 0), (4, 0)]
    
    def is_game_over(self):
        if self.killed_goat <5 and not self.can_move():
            print(self.killed_goat <5 , not self.can_move())
            # print(self.can_any_t_move())
            return True ,'Goat'
        elif self.killed_goat >=5:
            return True,'Tiger'
        else:
            return False,None
        

    def isvalid_move(self, from_, to_):
        # Handle the special '*' move
        if from_ == ('*', '*'):
            # Check if the target position is empty
            if self.board[to_[0]][to_[1]] == '_':
                return True
            # Move to positions with 'T' or 'G' are invalid
            if self.board[to_[0]][to_[1]] in ('T', 'G'):
                return False

        # Extract positions
        from_row, from_col = from_
        to_row, to_col = to_

        rows = len(self.board)
        cols = len(self.board[0])
        
        # Check if the positions are within bounds
        if not (0 <= from_row < rows and 0 <= from_col < cols):
            return False
        if not (0 <= to_row < rows and 0 <= to_col < cols):
            return False
        
        # Check if the positions are not blocked by obstacles
        if self.board[from_row][from_col] == '#':
            return False
        if self.board[to_row][to_col] == '#':
            return False
        
        # Special case for 'a' at (0, 2)
        special_positions = [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4)]
        if (from_ == (0, 2) and to_ in special_positions) or (to_ == (0, 2) and from_ in special_positions):
            return True

        # Calculate the difference in rows and columns
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        # Check if the move is valid (adjacent or two steps away)
        if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
            return True
        elif (row_diff == 2 and col_diff == 0) or (row_diff == 0 and col_diff == 2):
            return True

        return False

            
            
    


# b=Board()
# # b.print_board()
# b.make_move(('*','*'),(0,2),'tiger')
# b.make_move(('*','*'),(1,2),'goat')
# b.make_move(('*','*'),(1,3),'goat')
# b.make_move(('*','*'),(1,1),'goat')


# # b.make_move(('*','*'),(2,1),'tiger')

# # b.make_move(('*','*'),(2,3),'tiger')
# # b.make_move(('*','*'),(1,2),'tiger')

# # b.make_move(('*','*'),(2,2),'tiger')
# # b.make_move(('*','*'),(2,1),'goat')
# # b.make_move(('*','*'),(2,3),'goat')
# # b.make_move(('*','*'),(1,2),'goat')
# # b.make_move(('*','*'),(3,2),'goat')

# # b.make_move(('*','*'),(2,0),'goat')
# # b.make_move(('*','*'),(4,2),'goat')
# # b.make_move(('*','*'),(0,2),'goat')
# # b.make_move(('*','*'),(2,4),'goat')
# # b.killed_goat = 5
# b.print_board()
# print(b.is_game_over())
# # b.make_move(('*','*'),(4,3),'tiger')
# # b.print_board()
# # print(b.is_game_over())




# print(b.tiger,b.goat,b.killed_goat)