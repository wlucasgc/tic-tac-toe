import pygame
from pygame.locals import *
from .checker import Checker, GameStatus
from .background import Background
from .event_handler import EventHandler
from .game_mode import GameMode
from .grid import Grid
from .images import ICON
from .log import Log
from .players.player_symbol import PlayerSymbol
from .settings import *


class TicTacToe:
    def __init__(self, game_mode: GameMode = GameMode.HUMAN_VS_HUMAN) -> None:
        # Configura a janela
        pygame.init()
        self.__window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(pygame.image.load(ICON))

        # Modo de Jogo
        self.__game_mode = game_mode

        # Cria o background
        self.__background = Background()

        # Cria a tabela
        self.__grid = Grid()

        # Verificador do jogo
        self.__checher = Checker(self.__grid)

        # Eventos
        self.__event_handler = EventHandler()
        self.__event_handler.add_event(QUIT, self.__close)
        self.__event_handler.add_event(K_ESCAPE, self.__reset)
        self.__event_handler.add_event(K_1, lambda: self.__play(1))
        self.__event_handler.add_event(K_2, lambda: self.__play(2))
        self.__event_handler.add_event(K_3, lambda: self.__play(3))
        self.__event_handler.add_event(K_4, lambda: self.__play(4))
        self.__event_handler.add_event(K_5, lambda: self.__play(5))
        self.__event_handler.add_event(K_6, lambda: self.__play(6))
        self.__event_handler.add_event(K_7, lambda: self.__play(7))
        self.__event_handler.add_event(K_8, lambda: self.__play(8))
        self.__event_handler.add_event(K_9, lambda: self.__play(9))

        # Clock
        self.__clock = pygame.time.Clock()

        self.__reset()


    def run(self) -> None:
        while True:
            # Captura os eventos
            self.__event_handler.loop()

            # Desenha os elementos
            self.__draw()
            
            # Controla os frames
            self.__clock.tick(FPS)
    

    def __draw(self):
        self.__background.draw(self.__window)
        self.__grid.draw(self.__window)
        self.__checher.draw(self.__window)

        # Atualiza a tela
        pygame.display.update()

    
    def __change_turn(self) -> None:
        if self.__player_turn == PlayerSymbol.X:
            self.__player_turn = PlayerSymbol.O

        elif self.__player_turn == PlayerSymbol.O:
            self.__player_turn = PlayerSymbol.X


    def __play(self, cell: int) -> None:
        if self.__checher.game_status() != GameStatus.IN_PROGRESS:
            Log.print('O jogo terminou')    
            return

        Log.print(f'O jogador {self.__player_turn.name} tentou marcar a célula {cell}')
        
        if not self.__grid.mark(self.__player_turn, cell):
            Log.print('A jogada não foi válida!')
            return
        
        Log.print('Jogada bem sucedida!')
        self.__change_turn()
        Log.print(f'Agora é a vez do jogador {self.__player_turn.name}')


    def __reset(self) -> None:
        Log.print('Resetando o jogo...')
        self.__grid.reset()
        self.__player_turn = PlayerSymbol.X


    def __close(self) -> None:
        Log.print('Fechando o jogo...')
        pygame.quit()
        exit()

