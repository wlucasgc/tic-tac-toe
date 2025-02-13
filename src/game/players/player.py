import pygame
from abc import ABC, abstractmethod
from .player_symbol import PlayerSymbol
from ..element_interface import IElement
from ..settings import *


class Player(IElement):
    def __init__(self, cell):
        self._cell = cell
        self._image: pygame.surface.Surface = None
    

    @abstractmethod
    def symbol(self) -> PlayerSymbol:
        pass


    def draw(self, window: pygame.surface.Surface) -> None:
        # Identifica os valores de x e y da célula
        cell_x = (self._cell - 1) % 3
        cell_y = (self._cell - 1) // 3

        # Offset em x
        if cell_x == 0:
            offset_x = self._image.get_size()[1] // 4
        
        elif cell_x == 2:
            offset_x = - self._image.get_size()[1] // 4
        
        else:
            offset_x = 0

        # Offser em y
        if cell_y == 0:
            offset_y = self._image.get_size()[1] // 4
        
        elif cell_y == 2:
            offset_y = - self._image.get_size()[1] // 4
        
        else:
            offset_y = 0

        # Posição x e y na tela
        x = cell_x * (WIDTH // 3) + (WIDTH // 3 - self._image.get_size()[0]) // 2 + offset_x
        y = HEIGHT - WIDTH + cell_y * (WIDTH // 3) + (WIDTH // 3 - self._image.get_size()[1]) // 2 + offset_y
        
        # Desenha a jogada na tela
        window.blit(self._image, pygame.rect.Rect(x, y, self._image.get_size()[0], self._image.get_size()[1]))    