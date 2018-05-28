class Car:
    def __init__(self,w):
    self.wheels=w

c1=Car(4)
print("c1 memory location",hex(id(c1)))