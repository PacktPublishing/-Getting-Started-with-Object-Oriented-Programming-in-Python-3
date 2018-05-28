class Car:
    def __init__(self):
        self.color = None
        self.type = None

    def fill(self, fuel):
        self.type = fuel

    def empty(self):
        self.type = None
		
redCar = Car()
redCar.color = "red"
redCar.type = "gas"
redCar.empty()
redCar.fill("petrol")