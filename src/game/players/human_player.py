from .player import Player, Symbol
# from ..grid import Grid


class HumanPlayer(Player):
    def __init__(self, symbol: Symbol):
        super().__init__(symbol)


    # def play(self, grid: Grid, index: int) -> None:
    #     print(index)