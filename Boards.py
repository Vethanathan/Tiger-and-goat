# from Validator import Validator
def find_coordinate_between(index1, index2):
        # Calculate the average of each dimension to find the midpoint
        x_coord = (index1[0] + index2[0]) / 2
        y_coord = (index1[1] + index2[1]) / 2
        if (int(x_coord),int(y_coord))  in (index1,index2):
            return False
        return (int(x_coord), int(y_coord))  # Return as integers


class Board:
    #board_vals= {'a': (0, 2), 'b': (1, 0), 'c': (1, 1), 'd': (1, 2), 'e': (1, 3), 'f': (1, 4), 'g': (1, 5), 'h': (2, 0), 'i': (2, 1), 'j': (2, 2), 'k': (2, 3), 'l': (2, 4), 'm': (2, 5), 'n': (3, 0), 'o': (3, 1), 'p': (3, 2), 'q': (3, 3), 'r': (3, 4), 's': (3, 5), 't': (4, 1), 'u': (4, 2), 'v': (4, 3), 'w': (4, 4)}
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
        
    def print_board(self):
        for i in range(5):
            for j in range(6):
                print(self.board[i][j], end=" ")
            print()
    def make_move(self,from_board,to_board,role):
        from_row, from_col = from_board
        to_row, to_col = to_board
        if not self.isvalid_move(from_board,to_board):
            raise Exception("Invalid Move")
        else:
            if role == 'tiger':
                if not from_board == ('*','*'):
                    tup = find_coordinate_between(from_board,to_board)
                if from_board==('*','*'):
                    if self.board[to_row][to_col] == 'G':
                        raise Exception("Invalid Move")
                    elif self.tiger!=0 and self.board[to_row][to_col]=='_':
                        self.board[to_row][to_col] = 'T'
                else:
                    if tup:
                        if self.board[from_row][from_col] == 'T' and self.board[tup[0]][tup[1]] == 'G':
                            self.goat -= 1
                            self.board[tup[0]][tup[1]] = '_'
                            self.board[from_row][from_col] = '_'
                            self.board[to_row][to_col] = 'T'
                        else:
                            raise Exception("Invalid Move")
                    else:
                        if self.board[from_row][from_col] == 'T' and self.board[to_row][to_col] =='_':
                            self.board[from_row][from_col] = '_'
                            self.board[to_row][to_col] = 'T'
            elif role == 'goat':
                if not from_board == ('*','*'):
                    tup = find_coordinate_between(from_board,to_board)
                if from_board==('*','*'):
                    if self.board[to_row][to_col] == 'T':
                        raise Exception("Invalid Move")
                    elif self.tiger!=0 and self.board[to_row][to_col]=='_':
                        self.board[to_row][to_col] = 'G'
                else:
                    if tup:
                        if self.board[from_row][to_col] == 'G' and self.board[tup[0]][tup[1]] == 'T':
                            self.tiger -= 1
                            self.board[tup[0]][tup[1]] = '_'
                            self.board[from_row][from_col] = '_'
                            self.board[to_row][to_col] = ' G'
                        else:
                            raise Exception("Invalid Move")
                    else:
                        if self.board[from_row][from_col] == 'G' and self.board[to_row][to_col] =='_':
                            self.board[from_row][from_col] = '_'
                            self.board[to_row][to_col] = 'G'
                

        
    def board_index(self):
        board_vals= {'a': (0, 2), 'b': (1, 0), 'c': (1, 1), 'd': (1, 2), 'e': (1, 3), 'f': (1, 4), 'g': (1, 5), 'h': (2, 0), 'i': (2, 1), 'j': (2, 2), 'k': (2, 3), 'l': (2, 4), 'm': (2, 5), 'n': (3, 0), 'o': (3, 1), 'p': (3, 2), 'q': (3, 3), 'r': (3, 4), 's': (3, 5), 't': (4, 1), 'u': (4, 2), 'v': (4, 3), 'w': (4, 4)}
        invalid_dest=[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (4, 0), (4, 0)]

    def isvalid_move(self,from_,to_):
        if from_ ==('*','*') and self.board[to_[0]][to_[1]] =='_':
            return True
    
        if from_ ==('*','*') and self.board[to_[0]][to_[1]] =='T':
            return False
        if from_ ==('*','*') and self.board[to_[0]][to_[1]] =='G':
            return False

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
            
            
    


b=Board()
b.print_board()
b.make_move(('*','*'),(0,2),'goat')
b.print_board()
b.make_move(('*','*'),(1,2),'tiger')
b.print_board()
b.make_move((0,2),(2,2),'goat')
b.print_board()



print(b.tiger,b.goat)