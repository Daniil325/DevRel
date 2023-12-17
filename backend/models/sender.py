from abc import ABC, abstractmethod


class Sender(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def send(self):
        pass
