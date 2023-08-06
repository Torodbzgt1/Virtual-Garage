# create a class named Vehicle
class Vehicle:
    # constructor
    def __init__(self, make, model, color, fuelType):
        # set the instance attributes to the given parameters
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        # set options to an empty list
        self.options = []

        # input the options from the user
        if input('Does your vehicle have power mirrors(y/n): ').lower() == 'y':
            self.options.append('power mirrors')
        if input('Does your vehicle have power locks(y/n): ').lower() == 'y':
            self.options.append('power locks')
        if input('Does your vehicle have remote start(y/n): ').lower() == 'y':
            self.options.append('remote start')
          if input('Does your vehicle have manual transmission(y/n): ').lower() == 'y':
            self.options.append('manual transmission')
        if input('Does your vehicle have backup camera(y/n): ').lower() == 'y':
            self.options.append('backup camera')
        if input('Does your vehicle have bluetooth(y/n): ').lower() == 'y':
            self.options.append('bluetooth')
        if input('Does your vehicle have cruise control(y/n): ').lower() == 'y':
            self.options.append('cruise control')
        if input('Does your vehicle parking sensors(y/n): ').lower() == 'y':
            self.options.append('parking sensors')
        if input('Does your vehicle have power windows(y/n): ').lower() == 'y':
            self.options.append('power windows')
    
    # accessor for the vehicle's make
    def getMake(self):
        return self.make
        
    # accessor for the vehicle's model
    def getModel(self):
        return self.model
        
    # accessor for the vehicle's color
    def getColor(self):
        return self.color
        
    # accessor for the vehicle's fuel type
    def getFuelType(self):
        return self.fuelType
        
    # accessor for the vehicle's options list
    def getOptions(self):
        return self.options
       
# create a class named Car that inherits the Vehicle class
class Car(Vehicle):
    # constructor
    def __init__(self, make, model, color, fuelType, engineSize, numDoors):
        # invoke the parent class constructor to set the common attributes
        super().__init__(make, model, color, fuelType)
        # set the additional instance attributes to the appropriate parameters
        self.engineSize = engineSize
        self.numDoors = numDoors

    # accessor for the car's engine size
    def getEngineSize(self):
        return self.engineSize

    # accessor for the car's number of doors
    def getNumDoors(self):
        return self.numDoors
               
# create a class named Pickup that inherits the Vehicle class
class Pickup(Vehicle):
    # constructor
    def __init__(self, make, model, color, fuelType, cabStyle, bedLength):
        # invoke the parent class constructor to set the common attributes
        super().__init__(make, model, color, fuelType)
        # set the additional instance attributes to the appropriate parameters
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    # accessor for the pickup's cab style
    def getCabStyle(self):
        return self.cabStyle

    # accessor for the pickup's bed length
    def getBedLength(self):
        return self.bedLength

# main function
def main():
    # declare an empty list to store the vehicles in the garage
    garage = []

    while True:
        # display the menu
        print("Menu:\n1. Add a car to the garage\n2. Add a pickup to the garage\n3. Exit")
        # input an option from the user
        option = int(input("Enter a choice: "))
        # validate the inputted choice
        while option < 1 or option > 3:
            # re-input for a valid choice if invalid
            option = int(input("Invalid choice! Try again: "))

        # break the loop if the user opts to exit
        if option == 3:
            break

        # input the common attributes of the vehicle
        make = input("Enter the make: ")
        model = input("Enter the model: ")
        color = input("Enter the color: ")
        fuel = input("Enter the fuel type: ")

        # if the user opts to add a car to the garage
        if option == 1:
            # input the car's engine size and number of doors
            engine = float(input("Enter size of engine: "))
            doors = int(input("Enter number of doors: "))

            # create and add a new Car object with the inputted details
            garage.append(Car(make, model, color, fuel, engine, doors))

        # else if the user opts to add a car to the garage
        elif option == 2:
            # input the pickup's cab style and bed length
            cab = input("Enter the cab style: ")
            bed = float(input("Enter the bed length: "))

            # create and add a new Pickup object with the inputted details
            garage.append(Pickup(make, model, color, fuel, cab, bed))
        
        print()

    # if the garage list is empty
    if len(garage) == 0:
        # print an error message
        print("The garage is empty!")
    # otherwise the garage list is not empty
    else:
        # print the garage list
        print("The vehicles in the garage include:")
        for vehicle in garage:
            # print the type of vehicle
            print(type(vehicle).__name__)

            # print the common attributes of the vehicle
            print("Make: " + vehicle.getMake())
            print("Model: " + vehicle.getModel())
            print("Color: " + vehicle.getColor())
            print("Fuel Type: " + vehicle.getFuelType())

            # if the current vehicle is a car
            if isinstance(vehicle, Car):
                print("Engine Size: " + str(vehicle.getEngineSize()) + " cc")
                print("Number of Doors: " + str(vehicle.getNumDoors()))
            # else if the current vehicle is a pickup
            elif isinstance(vehicle, Pickup):
                print("Cab Style: " + vehicle.getCabStyle())
                print("Bed Length: " + str(vehicle.getBedLength()) + " foot")

            # print the feature options
            print("Features: ", end = "")
            print(", ".join(vehicle.getOptions()))
            print()

# call the main function
if __name__ == "__main__":
    main()