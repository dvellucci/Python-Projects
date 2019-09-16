class Board:
    def __init__(self, board, parent, cost, depth):
        self.board = board
        self.parent = parent
        self.cost = cost
        self.depth = depth
        self.actions = list()

    #Define each of the possible moves and return a new board if its successful
    def up(self):
        pos = self.board.index(0)
        if pos in (0, 1, 2):
            return None
        else:
            new_board = list(self.board)
            new_board[pos], new_board[pos-3] = new_board[pos-3], new_board[pos]
            return Board(new_board, self, self.cost + 1, self.depth + 1)

    def down(self):
        pos = self.board.index(0)
        if pos in (6, 7, 8):
            return None
        else:
            new_board = list(self.board)
            new_board[pos], new_board[pos+3] = new_board[pos+3], new_board[pos]
            return Board(new_board, self, self.cost + 1, self.depth + 1) 
    
    def left(self):
        pos = self.board.index(0)
        if pos in (0, 3, 6):
            return None
        else:
            new_board = list(self.board)
            new_board[pos], new_board[pos-1] = new_board[pos-1], new_board[pos]
            return Board(new_board, self, self.cost + 1, self.depth + 1)

    def right(self):
        pos = self.board.index(0)
        if pos in (2, 5, 8):
            return None
        else:
            new_board = list(self.board)
            new_board[pos], new_board[pos+1] = new_board[pos+1], new_board[pos]
            return Board(new_board, self, self.cost + 1, self.depth + 1)

    #get every possible child of the node
    def successors(self):
        succ = []

        up = self.up()
        if up is not None:
            succ.append(up)

        down = self.down()
        if down is not None:
            succ.append(down)

        left = self.left()
        if left is not None:
            succ.append(left)
        
        right = self.right()
        if right is not None:
            succ.append(right)

        return succ


    #does a goal test to see if the board equals a sorted board
    def goal_test(self):
        return self.board == sorted(self.board)

    


    