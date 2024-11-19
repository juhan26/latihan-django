class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"starting engine of {self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def start_engine(self):
        print(f"car engine started: {self.year} {self.make} {self.model}")

class MotorCycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def start_engine(self):
        print(f"motorcycle engine started: {self.year} {self.make} {self.model}")




car = Car("Toyota", "Corolla", 2023)
motorcycle = MotorCycle("Yamaha", "R15", 2022)

car.start_engine()
motorcycle.start_engine()
