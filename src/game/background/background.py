import pygame
from ..element_interface import IElement
from ..settings import HEIGHT, WIDTH


class Background(IElement):
    def draw(self, window: pygame.surface.Surface):
        window.fill(
            pygame.color.Color(200, 200, 200),
            pygame.rect.Rect(0, 0, WIDTH, HEIGHT)
        )



