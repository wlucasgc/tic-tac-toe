import pygame
from .cell_value import CellValue
from ..graphic_element_interface import IGraphicElement
from ..players import Symbol, XO, X, O


class Cell(IGraphicElement):
    def __init__(self, index: int):
        self.__index = index
        self.__player: XO = None

    
    def index(self) -> int:
        return self.__index
    

    def value(self) -> CellValue:
        if self.__player is None:
            return CellValue.EMPTY
        
        if self.__player.symbol() == Symbol.X:
            return CellValue.PLAYER_X
        
        if self.__player.symbol() == Symbol.O:
            return CellValue.PLAYER_O


    def change_value(self, value: CellValue) -> None:
        if value == CellValue.PLAYER_X:
            self.__player = X(self.__index)
            return
        
        if value == CellValue.PLAYER_O:
            self.__player = O(self.__index)
            return
        
        self.__player = None


    def draw(self, window: pygame.surface.Surface):
        if self.__player is None:
            return
        
        self.__player.draw(window)