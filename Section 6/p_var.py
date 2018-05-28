class car:

    __topspeed = 0
    __name=""

    def __init__(self):
	    self.__topspeed=250
	    self.name="SAM"
		
    def drive(self):
        print("Drive Top Speed=" +str(self.__topspeed))
		
    def setTopSpeed(self,speed):
        self.__topspeed=speed

volvo=car()
volvo.drive()
volvo.setTopSpeed(380)
volvo.drive()