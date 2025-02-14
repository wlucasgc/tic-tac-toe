import pygame
from .cell import Cell
from .cell_value import CellValue
from ..graphic_element_interface import IGraphicElement
from ..images import GRID
from ..players.symbol import Symbol
from ..settings import *


class Grid(IGraphicElement):    
    def __init__(self):
        self.__image = pygame.transform.scale(
            pygame.image.load(GRID),
            (int(0.9 * WIDTH), int(0.9 * WIDTH))
        )

        self.reset()
        

    def mark(self, symbol: Symbol, index: int) -> bool:
        if not index in self.free_cells():
            return False

        cell = self.__grid[index - 1]

        if symbol == Symbol.X:
            cell.change_value(CellValue.PLAYER_X)

        elif symbol == Symbol.O:
            cell.change_value(CellValue.PLAYER_O)
        
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
            cell.draw(window)

    
    def free_cells(self) -> list[int]:
        indexes: list[int] = []
        
        for cell in self.__grid:
            if cell.value() == CellValue.EMPTY:
                indexes.append(cell.index())

        return indexes
    

    def status(self) -> list[CellValue]:
        return [cell.value() for cell in self.__grid]
        

    def reset(self) -> None:
        self.__grid = [Cell(i + 1) for i in range(9)]