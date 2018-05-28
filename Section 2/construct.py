class Car:
	#construct - paramterized constuctor
    def __init__(self,name):
        print("This is parameterized constructor")
        self.name=name
	
    def model(self):
        print("my first car",self.name)
	
volvo=Car("Volvo S90")
volvo.model()
