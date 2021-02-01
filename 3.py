class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


my_worker = Position('Ivan', 'Sidorov', 'driver', 15000, 5000)
my_worker.get_full_name()
my_worker.get_total_income()
