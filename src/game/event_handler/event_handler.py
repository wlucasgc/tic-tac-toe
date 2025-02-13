import pygame
from pygame.locals import KEYDOWN
from typing import Callable


class EventHandler:
    def __init__(self):
        self.__events = {}

    
    def add_event(self, key_action: int, event: Callable[[], None]) -> None:
        self.__events[key_action] = event


    def loop(self):
        for event in pygame.event.get():
            event_code = event.dict.get('key') if event.type == KEYDOWN else event.type
            
            if self.__events.get(event_code) is not None:
                self.__events.get(event_code)()



