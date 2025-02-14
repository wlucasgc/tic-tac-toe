from abc import abstractmethod
from .player_interface import IPlayer, Symbol


class Player(IPlayer):
    def __init__(self, symbol: Symbol):
        self.__symbol = symbol

    
    def symbol(self) -> Symbol:
        return self.__symbol
        