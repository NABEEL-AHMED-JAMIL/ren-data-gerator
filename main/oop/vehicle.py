class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} is starting."


class Car(Vehicle): # Inherits Vehicle

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting."


if __name__ == '__main__':
    car = Car("Toyota", "Corolla")
    print(car.start())