class Car:
    def start(self):
        print("Car started")
	
    def reverse(self):
        print("Car taking reverse")
		
    def speed(self):
	    print("top speed = 200")

def main():
    volvo=Car()
    volvo.start()
    volvo.reverse()
    volvo.speed()
   
if __name__ == "__main__":
    main()