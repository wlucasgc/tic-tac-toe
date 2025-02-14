import pygame
import random
from .xo import XO, Symbol
from ..images import PLAYER_X
from ..settings import WIDTH


class X(XO):
    def __init__(self, index):
        super().__init__(index)

        self._image = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(PLAYER_X),
                (int(0.2 * WIDTH), int(0.2 * WIDTH))
            ),
            random.choice([0, 90, 180, 270])
        )
    

    def symbol(self) -> Symbol:
        return Symbol.X