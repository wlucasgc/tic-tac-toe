import random
from .player import Player, Symbol
# from ..grid import Grid


class CPUPlayerRandom(Player):
    def __init__(self, symbol: Symbol):
        super().__init__(symbol)


    # def play(self, grid: Grid, index: int) -> None:
    #     cell = self.__choose(grid)
    #     print(cell)
        
    #     grid.mark(self.symbol(), index)
        

    # def __choose(self, grid: Grid) -> int:
    #     return random.choice(grid.free_cells())