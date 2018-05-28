class Car:

    # Class variables
    vehicle_type = "suv"
    model = "S90"

    # Constructor method with instance variables brand and cost
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    # Method with instance variable followers
    def fan_follow(self, follow):
        print("This user has " + str(follow) + " follow")


def main():
    # First object, set up instance variables of constructor method
    car = Car("Volvo", 7)

    # Print out instance variable brand
    print(car.brand)

    # Print out class variable cost
    print(car.cost)

    # Second object
    suv = Car("Audi", 15)

    # Print out instance variable brand
    print(suv.brand)
    print(suv.cost)

    # Use set_followers method and pass followers instance variable
    suv.fan_follow(77)

    # Print out class variable vehicle_type
    print(suv.vehicle_type)

if __name__ == "__main__":
    main()
