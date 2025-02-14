import pygame
from pygame.locals import *
from .checker import Checker, GameStatus
from .background import Background
from .event_handler import EventHandler
from .grid import Grid
from .images import ICON
from .log import Log
from .players import PlayerFactory, PlayerType, Symbol
from .settings import *


class TicTacToe:
    def __init__(self, player_x_type = PlayerType.HUMAN, player_o_type = PlayerType.HUMAN) -> None:
        # Configura a janela
        pygame.init()
        self.__window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(pygame.image.load(ICON))

        # Cria os jogadores
        self.__player_x = PlayerFactory.create_player(player_x_type, Symbol.X)
        self.__player_y = PlayerFactory.create_player(player_o_type, Symbol.O)

        # Cria o background
        self.__background = Background()

        # Cria a tabela
        self.__grid = Grid()

        # Verificador do jogo
        self.__checher = Checker(self.__grid)

        # Clock
        self.__clock = pygame.time.Clock()

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
        if self.__turn == Symbol.X:
            self.__turn = Symbol.O

        elif self.__turn == Symbol.O:
            self.__turn = Symbol.X


    def __play(self, index: int) -> None:
        if self.__checher.game_status() != GameStatus.IN_PROGRESS:
            Log.print('O jogo terminou')    
            return

        Log.print(f'O jogador {self.__turn.name} tentou marcar a célula {index}')
        
        if not self.__grid.mark(self.__turn, index):
            Log.print('A jogada não foi válida!')
            return
        
        Log.print('Jogada bem sucedida!')
        self.__change_turn()
        Log.print(f'Agora é a vez do jogador {self.__turn.name}')


    def __reset(self) -> None:
        Log.print('Resetando o jogo...')
        self.__grid.reset()
        self.__turn = Symbol.X


    def __close(self) -> None:
        Log.print('Fechando o jogo...')
        pygame.quit()
        exit()

