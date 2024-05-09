import numpy as np
from player import Player
class Board:
    _nb_playing=0

    def __init__(self,row:int,col:int) -> None:
        self.row=row
        self.col=col

        self._board = np.zeros((self.row, self.col))
        self._list_players : list[Player] = []

    def __repr__(self):
        rpr = ""
        rpr += str(self._board)
        rpr+= "\n"
        rpr += str(self._list_players)
        return rpr

    def get_board(self):
        return self._board.shape

    def add_player(self, player: Player):
        self._list_players.append(player)

    def get_list_players(self):
        return self._list_players

    def insert_piece(self,player:Player):
        print(player.get_name()+"'s turn")
        col= int(input("Choose a column "))
        while col>=self.get_board()[1]:
            print(f"Column {col} does not exist, Choose another column")
            col= int(input("Choose a another column "))

        if self._board[0][col] == 0:                        
            for i in range(self.get_board()[0] -1,-1, -1):
                if self._board[i][col] == 0:
                    self._board[i][col] = player.get_symbol()
                    break
        else:
            print(f"Column {col} is full, Choose another column")
            self.insert_piece(player)
        
    def check_for_game_ending(self,symbol):
        #Check Horizontal
        for i in range(self.get_board()[0]):
            for j in range(self.get_board()[1]-3):
                if self._board[i][j] == symbol and self._board[i][j+1] == symbol and self._board[i][j+2] == symbol and self._board[i][j+3] == symbol:
                    return True
      
        #Check Vertical
        for j in range(self.get_board()[1]):
            for i in range(self.get_board()[0]-3):
                if self._board[i][j] == symbol and self._board[i+1][j] == symbol and self._board[i+2][j] == symbol and self._board[i+3][j]== symbol:
                    return True
           

        #Check Diagonals descending
        for i in range(self.get_board()[0]-3):
            for j in range(self.get_board()[1]-3):
                if self._board[i][j] == symbol and self._board[i+1][j+1] == symbol and self._board[i+2][j+2] == symbol and self._board[i+3][j+3] == symbol:
                    return True

        #Check Diagonals Ascending
        for j in range(self.get_board()[1]-3):
            for i in range(self.get_board()[0]-1,-3,-1):
                if self._board[i][j] == symbol and self._board[i-1][j+1] == symbol and self._board[i-2][j+2] == symbol and self._board[i-3][j+3] == symbol:
                    return True