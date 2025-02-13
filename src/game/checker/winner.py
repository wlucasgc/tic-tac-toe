from .winner_direction import WinnerDirection
from ..players.player_symbol import PlayerSymbol


class Winner:
    def __init__(self, player: PlayerSymbol, direction: WinnerDirection, number: int):
        self.__player = player
        self.__direction  = direction
        self.__number = number


    def player(self) -> PlayerSymbol:
        return self.__player
    

    def direction(self) -> WinnerDirection:
        return self.__direction
    

    def number(self) -> int:
        return self.__number