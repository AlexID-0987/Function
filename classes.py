class Car():
    def __init__(self, model, price) -> None:
        self.mod=model
        self.pr=price

cars=Car('Toyota',234567)
print(cars.mod, cars.pr)