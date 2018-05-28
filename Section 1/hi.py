class Man:
    def sayHi(self,name=None):
        if name is not None:
	        print("Hi " + name)
        else:
	        print("Hi!")
		
obj = Man()
obj.sayHi()
obj.sayHi("James")