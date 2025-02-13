import pygame
from abc import ABC, abstractmethod


class IElement(ABC):
    @abstractmethod
    def draw(self, window: pygame.surface.Surface) -> None:
        pass