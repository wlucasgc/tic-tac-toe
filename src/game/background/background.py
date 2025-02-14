import pygame
from ..graphic_element_interface import IGraphicElement
from ..settings import HEIGHT, WIDTH


class Background(IGraphicElement):
    def draw(self, window: pygame.surface.Surface):
        window.fill(
            pygame.color.Color(200, 200, 200),
            pygame.rect.Rect(0, 0, WIDTH, HEIGHT)
        )



