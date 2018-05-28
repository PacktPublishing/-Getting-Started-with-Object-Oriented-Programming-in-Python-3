class car(object):
    
    def __init__(self):
        self.__mileage = 16
        
    def getMileage(self):
        print(self.__mileage)
        
    def setMileage(self,mileage):
        self.__mileage = mileage
        
volvo = car()
volvo.getMileage()
volvo.setMileage(20)
volvo.getMileage()