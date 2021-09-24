from abc import ABCMeta
from abc import abstractmethod

class AbstractDuck(metaclass=ABCMeta):
    @abstractmethod
    def Quack(self):
        pass

class Duck(AbstractDuck):
    def Quack(self):
        print("[Duck] Quack")

duck = Duck()
duck.Quack()
