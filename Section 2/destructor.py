class Car:
    def __init__(self):
        print("Car created")
	
    def __del__(self):
        print("Destructor is called, Car is deleted")

volvo=Car()
del volvo