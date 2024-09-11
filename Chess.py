import random

class Piece:
    def __init__(self, player, board):
        self.board = board
        self.player = player
    
    def space_occupied(self, coords):
        i, j = coords
        if self.board[i][j] == None:
            return 0
        return self.board[i][j].player
    
    def is_valid(self, i, j):
        return True if (0 <= i <= 7 and 0 <= j <= 7) else False


class Pawn(Piece):
    def __init__(self, player, coordinates, board):
        super().__init__(player, board)
        self.isRemoved = False
        self.coordinates = coordinates
        self.symbol = "P"
        self.isFirstMove = True
    
    # if it reaches end, it can be promoted
    def valid_moves(self):
        i, j = self.coordinates
        possible_spots = []
        if self.player == 2: # coming from the top to bottom
            if self.is_valid(i+1, j) and self.space_occupied((i + 1, j)) == 0:
                possible_spots.append((i + 1, j))
                if self.isFirstMove and self.is_valid(i+2, j) and self.space_occupied((i + 2, j)) == 0:
                    possible_spots.append((i + 2, j))
            if self.is_valid(i+1, j-1) and self.space_occupied((i + 1, j-1)) == 1:
                possible_spots.append((i+1, j-1))
            if self.is_valid(i+1, j+1) and self.space_occupied((i + 1, j+1)) == 1:
                possible_spots.append((i+1, j+1))
        else: # coming from bottom to top
            if self.is_valid(i-1, j) and self.space_occupied((i - 1, j)) == 0:
                possible_spots.append((i - 1, j))
                if self.isFirstMove and self.is_valid(i-2, j) and self.space_occupied((i - 2, j)) == 0:
                    possible_spots.append((i - 2, j))
            if self.is_valid(i-1, j-1) and self.space_occupied((i - 1, j-1)) == 2:
                possible_spots.append((i-1, j-1))
            if self.is_valid(i-1, j+1) and self.space_occupied((i - 1, j+1)) == 2:
                possible_spots.append((i-1, j+1))
        return possible_spots if possible_spots else None
        
        
            
class Queen(Piece):
    def __init__(self, player, coordinates, board):
        super().__init__(player, board)
        self.isRemoved = False
        self.coordinates = coordinates
        self.symbol = "Q"
    def valid_moves(self):
        i, j = self.coordinates
        possible_spots = []
        
        c = 1
        while self.is_valid(i+c, j+c) and self.space_occupied((i+c, j+c)) == 0:
            possible_spots.append((i+c, j+c))
            c += 1
        if self.is_valid(i+c, j+c) and self.player != self.space_occupied((i+c, j+c)):
            possible_spots.append((i+c, j+c))
        
        c = 1
        while self.is_valid(i+c, j-c) and self.space_occupied((i+c, j-c)) == 0:
            possible_spots.append((i+c, j-c))
            c += 1
        if self.is_valid(i+c, j-c) and self.player != self.space_occupied((i+c, j-c)):
            possible_spots.append((i+c, j-c))
        
        c = 1
        while self.is_valid(i-c, j+c) and self.space_occupied((i-c, j+c)) == 0:
            possible_spots.append((i-c, j+c))
            c += 1
        if self.is_valid(i-c, j+c) and self.player != self.space_occupied((i-c, j+c)):
            possible_spots.append((i-c, j+c))
        
        c = 1
        while self.is_valid(i-c, j-c) and self.space_occupied((i-c, j-c)) == 0:
            possible_spots.append((i-c, j-c))
            c += 1
        if self.is_valid(i-c, j-c) and self.player != self.space_occupied((i-c, j-c)):
            possible_spots.append((i-c, j-c))
        
        
        c = 1
        while self.is_valid(i, j-c) and self.space_occupied((i, j-c)) == 0:
            possible_spots.append((i, j+c))
            c += 1
        if self.is_valid(i, j-c) and self.player != self.space_occupied((i, j-c)):
            possible_spots.append((i, j-c))
        
        c = 1
        while self.is_valid(i, j+c) and self.space_occupied((i, j+c)) == 0:
            possible_spots.append((i, j+c))
            c += 1
        if self.is_valid(i, j+c) and self.player != self.space_occupied((i, j+c)):
            possible_spots.append((i, j+c))
        
        c = 1
        while self.is_valid(i+c, j) and self.space_occupied((i+c, j)) == 0:
            possible_spots.append((i+c, j))
            c += 1
        if self.is_valid(i+c, j) and self.player != self.space_occupied((i+c, j)):
            possible_spots.append((i+c, j))
        
        c = 1
        while self.is_valid(i-c, j) and self.space_occupied((i-c, j)) == 0:
            possible_spots.append((i-c, j))
            c += 1
        if self.is_valid(i-c, j) and self.player != self.space_occupied((i-c, j)):
            possible_spots.append((i-c, j))

        return possible_spots if possible_spots else None         
    

class King(Piece):
    def __init__(self, player, coordinates, board):
        super().__init__(player, board)
        self.isRemoved = False
        self.coordinates = coordinates
        self.symbol = "K"
    
    def valid_moves(self):
        i, j = self.coordinates
        possible_spots = []
        coordinates_list = [(i+1, j+1), (i+1, j), (i+1, j-1), (i-1, j+1), (i-1, j), (i-1, j-1), (i, j+1), (i, j-1)]
        for coordinates in coordinates_list:
            s, k = coordinates
            if self.is_valid(s, k) and (self.space_occupied(coordinates) != self.player):
                possible_spots.append(coordinates)
        return possible_spots if possible_spots else None


class Rook(Piece):
    def __init__(self, player, coordinates, board):
        super().__init__(player, board)
        self.isRemoved = False
        self.coordinates = coordinates
        self.symbol = "R"
    def valid_moves(self):
        i, j = self.coordinates
        # it can move left, right, top, bottom
        possible_spots = []
        # check left
        c = 1
        while self.is_valid(i, j-c) and self.space_occupied((i, j-c)) == 0:
            possible_spots.append((i, j-c))
            c += 1
        if self.is_valid(i, j-c) and self.player != self.space_occupied((i, j-c)):
            possible_spots.append((i, j-c))
        
        c = 1
        while self.is_valid(i, j+c) and self.space_occupied((i, j+c)) == 0:
            possible_spots.append((i, j+c))
            c += 1
        if self.is_valid(i, j+c) and self.player != self.space_occupied((i, j+c)):
            possible_spots.append((i, j+c))
        
        c = 1
        while self.is_valid(i+c, j) and self.space_occupied((i+c, j)) == 0:
            possible_spots.append((i+c, j))
            c += 1
        if self.is_valid(i+c, j) and self.player != self.space_occupied((i+c, j)):
            possible_spots.append((i+c, j))
        
        c = 1
        while self.is_valid(i-c, j) and self.space_occupied((i-c, j)) == 0:
            possible_spots.append((i-c, j))
            c += 1
        if self.is_valid(i-c, j) and self.player != self.space_occupied((i-c, j)):
            possible_spots.append((i-c, j))

        return possible_spots if possible_spots else None

class Bishop(Piece):
    def __init__(self, player, coordinates, board):
        super().__init__(player, board)
        self.isRemoved = False
        self.coordinates = coordinates
        self.symbol = "B"
    
    def valid_moves(self):
        i, j = self.coordinates
        possible_spots = []
        c = 1
        while self.is_valid(i+c, j+c) and self.space_occupied((i+c, j+c)) == 0:
            possible_spots.append((i+c, j+c))
            c += 1
        if self.is_valid(i+c, j+c) and self.player != self.space_occupied((i+c, j+c)):
            possible_spots.append((i+c, j+c))
        
        c = 1
        while self.is_valid(i+c, j-c) and self.space_occupied((i+c, j-c)) == 0:
            possible_spots.append((i+c, j-c))
            c += 1
        if self.is_valid(i+c, j-c) and self.player != self.space_occupied((i+c, j-c)):
            possible_spots.append((i+c, j-c))
        
        c = 1
        while self.is_valid(i-c, j+c) and self.space_occupied((i-c, j+c)) == 0:
            possible_spots.append((i-c, j+c))
            c += 1
        if self.is_valid(i-c, j+c) and self.player != self.space_occupied((i-c, j+c)):
            possible_spots.append((i-c, j+c))
        
        c = 1
        while self.is_valid(i-c, j-c) and self.space_occupied((i-c, j-c)) == 0:
            possible_spots.append((i-c, j-c))
            c += 1
        if self.is_valid(i-c, j-c) and self.player != self.space_occupied((i-c, j-c)):
            possible_spots.append((i-c, j-c))
        
        return possible_spots if possible_spots else None
    

class Knight(Piece):
    def __init__(self, player, coordinates, board):
        super().__init__(player, board)
        self.isRemoved = False 
        self.coordinates = coordinates 
        self.symbol = "N"
    def valid_moves(self):
        i, j = self.coordinates
        possible_spots = []
        coordinates_list = [(i + 2, j - 1), (i + 2, j + 1), (i - 2, j - 1), (i - 2, j + 1), (i - 1, j + 2), (i - 1, j - 2), (i + 1, j + 2), (i + 1, j - 2)]
        for coordinates in coordinates_list:
            s, k = coordinates
            if self.is_valid(s, k) and (self.space_occupied(coordinates) != self.player):
                possible_spots.append(coordinates)
        return possible_spots if possible_spots else None
                

# need to check for pawn promotion
# need to determine when to draw
# determine checkmate

class Game:
    def __init__(self):
        self.board = [[None, None, None, None, None, None, None, None] for i in range(8)]
        self.player_2_pieces = [Rook(2, (0, 0), self.board), Knight(2, (0, 1), self.board), Bishop(2, (0, 2), self.board), Queen(2, (0, 3), self.board), King(2, (0, 4), self.board), Bishop(2, (0, 5), self.board), Knight(2, (0, 6), self.board), Rook(2, (0, 7), self.board), Pawn(2, (1, 0), self.board), Pawn(2, (1, 1), self.board), Pawn(2, (1, 2), self.board), Pawn(2, (1, 3), self.board), Pawn(2, (1, 4), self.board), Pawn(2, (1, 5), self.board), Pawn(2, (1, 6), self.board), Pawn(2, (1, 7), self.board)]
        self.player_1_pieces = [Rook(1, (7, 0), self.board), Knight(1, (7, 1), self.board), Bishop(1, (7, 2), self.board), Queen(1, (7, 3), self.board), King(1, (7, 4), self.board), Bishop(1, (7, 5), self.board), Knight(1, (7, 6), self.board), Rook(1, (7, 7), self.board), Pawn(1, (6, 0), self.board), Pawn(1, (6, 1), self.board), Pawn(1, (6, 2), self.board), Pawn(1, (6, 3), self.board), Pawn(1, (6, 4), self.board), Pawn(1, (6, 5), self.board), Pawn(1, (6, 6), self.board), Pawn(1, (6, 7), self.board)]

        self.player_1_king = None
        self.player_2_king = None

        for piece in (self.player_2_pieces + self.player_1_pieces):
            i, j = piece.coordinates
            self.board[i][j] = piece
            if piece.player == 1 and piece.symbol == "K":
                self.player_1_king = piece
            if piece.player == 2 and piece.symbol == "K":
                self.player_2_king = piece
        
        self.curr_player = 1
        self.winner = None
        self.finished = False
    
    def print_board(self):
        board = [['ij', '0 ', '1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ']]
        for i in range(8):
            board.append([f'{i}',"--", "--", "--", "--", "--", "--", "--", "--"])
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
              if self.board[i][j]:
                  board[i+1][j+1] = str(self.board[i][j].player) + self.board[i][j].symbol
        lines = []
        for r in board:
            line = " ".join(r)
            lines.append(line)
        res = "\n".join(lines)
        print(res)

    def check_for_checkmate(self):
        self.check_king(self.player_1_king)
        self.check_king(self.player_2_king)

    def check_king(self, king):
        # determine the valid moves that the king can move to
        king_moves = king.valid_moves()
        if not king_moves:
          return
        pieces = self.player_1_pieces if king.player == 2 else self.player_2_pieces
        all_moves = []
        for piece in pieces:
            curr_moves = piece.valid_moves()
            if curr_moves:
              all_moves += piece.valid_moves()
        if king.coordinates not in all_moves:
            return
        for move in king_moves:
            if move not in all_moves:
                return
        print("Checkmate!")
        self.winner = king.player
        self.finished = True
    
    def remove_piece(self, piece, i, j):
        if piece.player == 1 and piece.space_occupied((i, j)) == 2:
            other_piece = self.board[i][j]
            self.player_2_pieces.remove(other_piece)
            if other_piece.symbol == "K":
                self.winner = 1
                self.finished = True
        if piece.player == 2 and piece.space_occupied((i, j)) == 1:
            other_piece = self.board[i][j]
            self.player_1_pieces.remove(other_piece)
            if other_piece.symbol == "K":
                self.winner = 2
                self.finished = True

    def move_piece(self, piece, new_coords):
        i, j = new_coords
        old_i, old_j = piece.coordinates
        piece.coordinates = new_coords
        # removes a piece if there is a piece
        self.remove_piece(piece, i, j)
        # make the previous spot empty
        self.board[old_i][old_j] = None
        self.board[i][j] = piece
        if piece.symbol == "P":
            piece.isFirstMove = False
        self.check_for_checkmate()
        self.print_board()
    
    def valid_input(self, msg):
        msg = msg.split(",")
        for i in range(len(msg)):
            msg[i] = msg[i].strip()
        if len(msg) != 4:
          return False, None
        for item in msg:
            if len(item) != 1 or item not in "01234567":
                return False, None
        if msg[0] == msg[1] and msg[2] == msg[3]:
            return False, None
        return True, msg

    def execute_move(self):
        msg = input("Input Move in following format: 'old_i, old_j, new_i, new_j': ")
        is_valid, msg = self.valid_input(msg)
        if is_valid:
            for i in range(len(msg)):
                msg[i] = int(msg[i])
            piece = self.board[msg[0]][msg[1]]
            if piece and piece.player == self.curr_player:
              move = (msg[2], msg[3])
              if move in piece.valid_moves():
                  self.move_piece(piece, move)
                  return
        self.execute_move()
    
    def random_move(self):
        random_piece = random.choice(self.player_2_pieces)
        valid_moves = random_piece.valid_moves()
        if not valid_moves:
            self.random_move()
        else:
            # randomly pick one of the random moves
            move = random.choice(valid_moves)
            self.move_piece(random_piece, move)


    def start_game(self):
        print("Let's play some chess!")
        self.print_board()
        players = 1
        while True:
            players = int(input("Input 1 for single-player mode and 2 for two-player mode: "))
            if players == 1 or players == 2:
                break
        while not self.finished:
            # player makes move
            if self.curr_player == 1:
                # ask to make a move
                self.execute_move()
                self.curr_player = 2
            else:
                if players == 1:
                  self.random_move()
                else:
                  self.execute_move()
                self.curr_player = 1
        print(f'Player {self.winner} won!')


if __name__ == "__main__":
    while True:
      game = Game()
      game.start_game()
      playAgain = input("Do you want to play again? [y/n]").strip().lower()
      if playAgain == "n":
          print("Thank you for playing!")
          break
