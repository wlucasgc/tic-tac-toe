import pygame
from .cell_values import CellValues
from ..element_interface import IElement
from ..players.player import Player
from ..players.player_x import PlayerX
from ..players.player_o import PlayerO
from ..players.player_symbol import PlayerSymbol
from ..settings import *


class Grid(IElement):    
    def __init__(self):
        self.__image = pygame.transform.scale(
            pygame.image.load('assets/table.png'),
            (int(0.9 * WIDTH), int(0.9 * WIDTH))
        )

        self.reset()
        

    def mark(self, player_turn: PlayerSymbol, cell: int) -> bool:
        if not cell in self.free_cells():
            return False
                
        if player_turn == PlayerSymbol.X:
            self.__grid[cell - 1] = PlayerX(cell)

        elif player_turn == PlayerSymbol.O:
            self.__grid[cell - 1] = PlayerO(cell)
        
        return True


    def draw(self, window: pygame.surface.Surface):
        window.blit(
            self.__image, 
            pygame.rect.Rect(
                (WIDTH - self.__image.get_size()[0]) // 2, 
                HEIGHT - WIDTH + (WIDTH - self.__image.get_size()[1]) // 2,
                WIDTH,
                WIDTH
            )
        )

        for cell in self.__grid:
            if cell is not None:
                cell.draw(window)

    
    def free_cells(self) -> list[int]:
        cells: list[int] = []
        
        for i in range(len(self.__grid)):
            if self.__grid[i] is None:
                cells.append(i + 1)

        return cells
    

    def status(self) -> list[CellValues]:
        values: list[CellValues] = []

        for cell in self.__grid:
            if cell is None:
                values.append(CellValues.EMPTY)
            
            elif cell.symbol() == PlayerSymbol.X:
                values.append(CellValues.PLAYER_X)
            
            elif cell.symbol() == PlayerSymbol.O:
                values.append(CellValues.PLAYER_O)
            
        return values


    def reset(self) -> None:
        self.__grid: list[Player] = [
            None, None, None,
            None, None, None,
            None, None, None,
        ]