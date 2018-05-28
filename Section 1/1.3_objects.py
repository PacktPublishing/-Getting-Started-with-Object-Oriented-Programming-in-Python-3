class Car:
   'Common base class for all cars'
   carCount = 0

   def __init__(self, name, year):
      self.name = name
      self.year = year
      Car.carCount += 1
   
   def displayCount(self):
     print ("Total Car %d" % Car.carCount)

   def displayCar(self):
      print ("Name : ", self.name,  ", Year: ", self.year)


#This would create first object of Car class"
car1 = Car("Honda", 2000)
#This would create second object of Car class"
car2 = Car("BMW", 2017)
car1.displayCar()
car2.displayCar()
print ("Total Car %d" % Car.carCount)