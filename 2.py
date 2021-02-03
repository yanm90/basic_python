from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def count(self):
        pass


class Coat(Clothes):
    @property
    def count(self):
        return round(self.param / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def count(self):
        return round(2 * self.param + 0.3, 2)


my_coat = Coat(45)
my_costume = Costume(1.72)

print(my_coat.count)
print(my_costume.count)
