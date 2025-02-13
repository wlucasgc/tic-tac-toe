from abc import ABC
from .settings import DEBUG


class Log(ABC):
    @staticmethod
    def print(text) -> None:
        if DEBUG:
            print(text)