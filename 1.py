from itertools import cycle
from time import sleep


class TrafficLight:
    __color = ('red', 'yellow', 'green')
    __count = 0

    def running(self, stop=100):
        for i in cycle(self.__color):
            if self.__count == stop:
                break
            else:
                if i == 'green':
                    sleep(2)
                else:
                    sleep(7)
                print(i)
                self.__count += 1


a1 = TrafficLight()
a1.running(6)
