import pygame
import random
from .player import Player
from .player_symbol import PlayerSymbol
from ..images import PLAYER_X
from ..settings import *


class PlayerX(Player):
    def __init__(self, cell):
        super().__init__(cell)

        self._image = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(PLAYER_X),
                (int(0.2 * WIDTH), int(0.2 * WIDTH))
            ),
            random.choice([0, 90, 180, 270])
        )
    

    def symbol(self) -> PlayerSymbol:
        return PlayerSymbol.X