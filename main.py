from board import Board
from player import Player


if __name__ == "__main__":
    
    boardx: Board = Board(6,7)

    player_1: Player = Player("Player 1", 1)
    player_2: Player = Player("Player 2", 2)

    boardx.add_player(player_1)
    boardx.add_player(player_2)

    print(boardx)
    turn =0
    game_over = False

    while game_over == False:
        if turn == 0:
            boardx.insert_piece(player_1)
            print(boardx)
            
            if boardx.check_for_game_ending(player_1.get_symbol()) == True:
                game_over = True
                print(player_1.get_name()+" is the winner")
            turn=1
        else:
            boardx.insert_piece(player_2)
            print(boardx)
            if boardx.check_for_game_ending(player_2.get_symbol())== True:
                game_over = True
                print(player_2.get_name()+" is the winner")
            turn=0

 

    
