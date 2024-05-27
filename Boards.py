# from Validator import Validator
class Board:
    board_vals= {'a': (0, 2), 'b': (1, 0), 'c': (1, 1), 'd': (1, 2), 'e': (1, 3), 'f': (1, 4), 'g': (1, 5), 'h': (2, 0), 'i': (2, 1), 'j': (2, 2), 'k': (2, 3), 'l': (2, 4), 'm': (2, 5), 'n': (3, 0), 'o': (3, 1), 'p': (3, 2), 'q': (3, 3), 'r': (3, 4), 's': (3, 5), 't': (4, 1), 'u': (4, 2), 'v': (4, 3), 'w': (4, 4)}
    invalid_dest=[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (4, 0), (4, 0)]
    

    def __init__(self):

        self.board =[
            ['#','#','a','#','#','#'],
            ['b','c','d','e','f','g'],
            ['h','i','j','k','l','m'],
            ['n','o','p','q','r','s'],
            ['#','t','u','v','w','#']
            ] 
        self.goat = 15
        self.tiger = 3
        
    def print_board(self):
        for i in range(5):
            for j in range(6):
                print(self.board[i][j], end=" ")
            print()
    def make_move(self,from_board,to_board):
        if not self.isvalid_move(from_board,to_board):
            raise Exception("Invalid Move")
        else:   
            pass

        
    def board_index(self):
        board_vals= {'a': (0, 2), 'b': (1, 0), 'c': (1, 1), 'd': (1, 2), 'e': (1, 3), 'f': (1, 4), 'g': (1, 5), 'h': (2, 0), 'i': (2, 1), 'j': (2, 2), 'k': (2, 3), 'l': (2, 4), 'm': (2, 5), 'n': (3, 0), 'o': (3, 1), 'p': (3, 2), 'q': (3, 3), 'r': (3, 4), 's': (3, 5), 't': (4, 1), 'u': (4, 2), 'v': (4, 3), 'w': (4, 4)}
        invalid_dest=[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (4, 0), (4, 0)]

    def isvalid_move(self,from_,to_):

        from_row, from_col = from_
        to_row, to_col = to_

        rows = len(self.board)
        cols = len(self.board[0])
        
        if not (0 <= from_row < rows and 0 <= from_col < cols):
            return False
        if not (0 <= to_row < rows and 0 <= to_col < cols):
            return False
        if self.board[from_row][from_col] == '#':
            return False
        if self.board[to_row][to_col] == '#':
            return False
        # special case for for 'a'
        if from_ ==(0,2) and to_ in [(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(2,4)]:
            return True

        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
            return True
        elif (row_diff == 2 and col_diff == 0) or (row_diff == 0 and col_diff == 2):
            return True
        
        return False
            
            
    


