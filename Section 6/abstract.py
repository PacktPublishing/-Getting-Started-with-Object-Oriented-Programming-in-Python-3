from abc import ABCMeta, abstractmethod

class Pet(metaclass=ABCMeta):

    @abstractmethod
    def pet_say(self):
	    return("I have a Pet!")
		
class Dog(Pet):
    def pet_say(self):
	    s = super(Dog, self).pet_say()
	    return print("%s - %s" % (s, "Borf!!"))
		
        
d = Dog()
d.pet_say()