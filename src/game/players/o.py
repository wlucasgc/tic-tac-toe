import pygame
import random
from .xo import XO, Symbol
from ..images import PLAYER_O
from ..settings import *


class O(XO):
    def __init__(self, cell):
        super().__init__(cell)
        
        self._image = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(PLAYER_O),
                (int(0.2 * WIDTH), int(0.2 * WIDTH))
            ),
            random.choice([0, 90, 180, 270])
        )


    def symbol(self) -> Symbol:
        return Symbol.O