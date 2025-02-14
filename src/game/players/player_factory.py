from abc import ABC
from .cpu_player_random import CPUPlayerRandom
from .human_player import HumanPlayer
from .player_interface import IPlayer
from .player_type import PlayerType
from .symbol import Symbol


class PlayerFactory(ABC):
    @staticmethod
    def create_player(player_type: PlayerType, symbol: Symbol) -> IPlayer:
        if player_type == PlayerType.HUMAN:
            return HumanPlayer(symbol)
        
        if player_type == PlayerType.CPU_RANDOM:
            return CPUPlayerRandom(symbol)

        if player_type == PlayerType.CPU_RL:
            raise NotImplementedError('Este jogador ainda não está disponível!')