from .winner_direction import WinnerDirection
from ..players.symbol import Symbol


class Winner:
    def __init__(self, player: Symbol, direction: WinnerDirection, number: int):
        self.__player = player
        self.__direction  = direction
        self.__number = number


    def player(self) -> Symbol:
        return self.__player
    

    def direction(self) -> WinnerDirection:
        return self.__direction
    

    def number(self) -> int:
        return self.__number