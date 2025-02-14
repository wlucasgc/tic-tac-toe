import pygame
from abc import ABC, abstractmethod


class IGraphicElement(ABC):
    @abstractmethod
    def draw(self, window: pygame.surface.Surface) -> None:
        pass