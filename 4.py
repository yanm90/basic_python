class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч')

    def change_speed(self, new_speed):
        self.speed = new_speed

    def go(self):
        self.speed = 5
        print(f'{self.name} тронулась')

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась')


class TownCar(Car):
    def __init__(self, name, color, speed, is_police, pas):
        super().__init__(name, color, speed, is_police)
        self.pas = pas

    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч')
        if self.speed > 60:
            print('Скорость превышена!')

    def station(self, change_pas):
        self.speed = 0
        self.pas += change_pas
        print(f'Количcтво пассажиров: {self.pas}')


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police, cargo):
        super().__init__(name, color, speed, is_police)
        self.cargo = cargo

    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч')
        if self.speed > 40:
            print('Скорость превышена!')

    def loading(self, load):
        self.cargo = load


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police, avtozak, siren):
        super().__init__(name, color, speed, is_police)
        self.avtozak = avtozak
        self.siren = siren

    def turn_on_siren(self):
        self.siren = True

    def turn_off_siren(self):
        self.siren = False

    def siren_status(self):
        if self.siren is True:
            print('Сирена включена')
        else:
            print('Сирена выключена')


class SportCar(Car):
    pass


car1 = Car('Toyota', 'Black', 70, False)
car1.show_speed()
car1.stop()
car1.go()
car1.show_speed()

print(''.join(['-' for _ in range(50)]))

bus = TownCar('Nefaz', 'White', 61, False, 35)
bus.show_speed()
bus.station(-10)

print(''.join(['-' for _ in range(50)]))

police_uaz = PoliceCar('UAZ', 'Special', 0, True, False, False)
police_uaz.turn_on_siren()
police_uaz.siren_status()

print(''.join(['-' for _ in range(50)]))

sport = SportCar('Ferrari', 'Red', 70, False)
sport.change_speed(225)
sport.show_speed()
