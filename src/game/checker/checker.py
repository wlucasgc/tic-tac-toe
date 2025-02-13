import pygame
from math import sqrt
from .game_status import GameStatus
from .winner import Winner, WinnerDirection
from ..grid.grid import CellValues, Grid
from ..players.player_symbol import PlayerSymbol
from ..element_interface import IElement
from ..images import LINE
from ..settings import *

class Checker(IElement):
    def __init__(self, grid: Grid):
        self.__grid = grid

        self.__image = pygame.transform.scale(
            pygame.image.load(LINE),
            (int(0.04 * WIDTH), WIDTH)
        ) 
        
        self.reset()
    

    def draw(self, window: pygame.surface.Surface) -> None:
        self.__check()
        
        if self.__winner is None:
            return
        
        x, y, angle = self.__coordinates()

        window.blit(
            pygame.transform.rotate(self.__image, angle),
            pygame.rect.Rect(x, y, self.__image.get_size()[0], self.__image.get_size()[1])
        )


    def game_status(self) -> GameStatus:
        if self.__winner is None:
            if len(self.__grid.free_cells()) == 0:
                return GameStatus.NO_WINNER
            
            return GameStatus.IN_PROGRESS
            
        if self.__winner.player() == PlayerSymbol.X:
            return GameStatus.PLAYER_X_WON
        
        if self.__winner.player() == PlayerSymbol.O:
            return GameStatus.PLAYER_O_WON


    def reset(self) -> None:
        self.__winner = None
    

    def __check(self):
        grid_status = self.__grid.status()
        
        # Procura um vencedor nas diagonais
        if grid_status[0] == CellValues.PLAYER_X and grid_status[4] == CellValues.PLAYER_X and grid_status[8] == CellValues.PLAYER_X: 
            self.__winner = Winner(PlayerSymbol.X, WinnerDirection.DIAGONAL, 1)
            return
                
        if grid_status[2] == CellValues.PLAYER_X and grid_status[4] == CellValues.PLAYER_X and grid_status[6] == CellValues.PLAYER_X:
            self.__winner = Winner(PlayerSymbol.X, WinnerDirection.DIAGONAL, 2)
            return
            
        if grid_status[0] == CellValues.PLAYER_O and grid_status[4] == CellValues.PLAYER_O and grid_status[8] == CellValues.PLAYER_O:
            self.__winner = Winner(PlayerSymbol.O, WinnerDirection.DIAGONAL, 1)
            return
        
        if grid_status[2] == CellValues.PLAYER_O and grid_status[4] == CellValues.PLAYER_O and grid_status[6] == CellValues.PLAYER_O:
            self.__winner = Winner(PlayerSymbol.O, WinnerDirection.DIAGONAL, 2)
            return
                
        # Procura um vencedor linha a linha
        for i in range(3):
            if grid_status[3 * i] == CellValues.PLAYER_X and grid_status[3 * i + 1] == CellValues.PLAYER_X and grid_status[3 * i + 2] == CellValues.PLAYER_X:
                self.__winner = Winner(PlayerSymbol.X, WinnerDirection.LINE, i + 1)
                return
            
            if grid_status[3 * i] == CellValues.PLAYER_O and grid_status[3 * i + 1] == CellValues.PLAYER_O and grid_status[3 * i + 2] == CellValues.PLAYER_O:
                self.__winner = Winner(PlayerSymbol.O, WinnerDirection.LINE, i + 1)
                return
        
        # Procura um vencedor coluna por coluna
        for i in range(3):
            if grid_status[i] == CellValues.PLAYER_X and grid_status[i + 3] == CellValues.PLAYER_X and grid_status[i + 6] == CellValues.PLAYER_X:
                self.__winner = Winner(PlayerSymbol.X, WinnerDirection.COLUMN, i + 1)
                return
            
            if grid_status[i] == CellValues.PLAYER_O and grid_status[i + 3] == CellValues.PLAYER_O and grid_status[i + 6] == CellValues.PLAYER_O:
                self.__winner = Winner(PlayerSymbol.O, WinnerDirection.COLUMN, i + 1)
                return
        
        self.__winner = None
        


    def __coordinates(self) -> tuple[int, int, int]:
        # Linha
        if self.__winner.direction() == WinnerDirection.LINE:
            x = 0
            y = (HEIGHT - WIDTH) + (WIDTH // 2) - (self.__image.get_size()[0] // 2)
            angle = 90

            if self.__winner.number() == 1:
                y -= int(0.29 * WIDTH)
                return x, y, angle

            if self.__winner.number() == 3:
                y += int(0.29 * WIDTH)
                return x, y, angle
        
            return x, y, angle            

        # Coluna
        if self.__winner.direction() == WinnerDirection.COLUMN:
            x = (WIDTH - self.__image.get_size()[0]) // 2
            y = HEIGHT - WIDTH
            angle = 0

            if self.__winner.number() == 1:
                x -= int(0.29 * WIDTH) 
                return x, y, angle
            
            if self.__winner.number() == 3:    
                x += int(0.29 * WIDTH) 
                return x, y, angle

            return x, y, angle
        
        # Diagonal
        if self.__winner.direction() == WinnerDirection.DIAGONAL:
            side = sqrt((self.__image.get_size()[1] ** 2) // 2)
            x = (WIDTH - side) // 2
            y = (HEIGHT - WIDTH) + ((WIDTH - side) // 2)

            if self.__winner.number() == 1:
                angle = 45
                return x, y, angle
        
            if self.__winner.number() == 2:
                y -= (self.__image.get_size()[0] // 2)
                angle = 135
                return x, y, angle
        