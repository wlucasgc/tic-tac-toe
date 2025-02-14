from abc import ABC, abstractmethod
from .symbol import Symbol
# from ..grid import Grid


class IPlayer(ABC):
    @abstractmethod
    def symbol(self) -> Symbol:
        pass


    # @abstractmethod
    # def play(self, grid: Grid, index: int):
    #     pass