from enum import Enum


class GameMode(Enum):
    HUMAN_VS_HUMAN = 0
    HUMAN_VS_CPU = 1
    CPU_VS_HUMAN = 2
    CPU_VS_CPU = 4