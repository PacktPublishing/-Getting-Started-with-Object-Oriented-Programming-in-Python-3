x=10
print(type(x))

y=x
if (id(x)==id(y)):
    print(" x and y are using same refernce object")

x=x+1
if (id(x)!=id(y)):
    print(" x and y are using different refernce object")
	
z=10
if (id(x)!=id(y)):
    print(" y and z are using same refernce object")
else:
    print(" y and z are using diffenent refernce object")