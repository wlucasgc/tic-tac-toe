from src.game import TicTacToe, PlayerType


if __name__ == '__main__':
    tictactoe = TicTacToe(
        player_x_type = PlayerType.HUMAN,
        player_o_type = PlayerType.HUMAN
    )
    
    tictactoe.run()