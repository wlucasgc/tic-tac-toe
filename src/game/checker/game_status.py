from enum import Enum


class GameStatus(Enum):
    IN_PROGRESS = 0
    PLAYER_X_WON = 1
    PLAYER_O_WON = 2
    NO_WINNER = 3