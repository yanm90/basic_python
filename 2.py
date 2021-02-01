class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, mass=25, thickness=5):
        print(f'Масса асфальта: {round(self._width * self._length * mass * thickness / 1000, 2)} тонн')


my_road = Road(5000, 20)
my_road.calculate_mass()
