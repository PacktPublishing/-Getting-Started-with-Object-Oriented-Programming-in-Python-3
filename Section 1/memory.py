Car1_price = 5000
print (Car1_price)

Car2_price = Car1_price
if (id(Car1_price) == id(Car2_price)):
    print("Car1 and Car2 have same object value & Memory ID = ", hex(id(Car1_price)))
    
Car1_price = Car1_price + 10
if (id(Car1_price) != id(Car2_price)):
    print("Car1 and Car2 have different object value & Memory ID = ", hex(id(Car1_price)),"&", hex(id(Car2_price)))
	
Car3_price = 5000
if (id(Car2_price)==id(Car3_price)):
    print("Car2 and Car3 have same memory value & Memory ID = ", hex(id(Car3_price)))
else:
    print("Car2 and Car3 have different object value & Memory ID = ", hex(id(Car3_price)))
	
Car1_price = None
print("Value is None")
print("Garbage Collector emptied the memory")