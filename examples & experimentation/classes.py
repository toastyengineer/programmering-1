"""
This program is the real deal ya'll

Important: metric system is used in all values, distance is in kilometres
classes.py
"""
import math

class Cars:
    """ This car class allows the creation of an endless amount of vehicles """
    def __init__(self, colour="White", chassis="Sedan", torque="Unspecified", consumption=0.8):
        """ Assigns the car with factory settings """
        self.colour = colour
        self.chassis = chassis
        self.torque = torque
        self.consumption = consumption # litres / 10 distance
        self.running = False
        self.fuel = 68  # litres
        self.pos = [0, 0]

    def __str__(self):
        """ What gets printed when you print an object from this class """
        return f"Colour: {self.colour} ; Type: {self.chassis} ; Torque: {self.torque} ; \
Running: {self.running} ; {round(self.fuel, 1)}L remaining ; Position: ({self.pos[0]},{self.pos[1]})"

    def start(self):
        """ Starts the engine """
        self.running = True

    def stop(self):
        """ Stops the engine """
        self.running = False

    def drive(self, pos):
        """ Moves the car to a coordinate"""
        if self.running and self.distance(pos) <= self.range():

            self.fuel =  self.fuel - (self.distance(pos)/ 10 * self.consumption)
            self.pos = pos

        return False

    def read_position(self):
        """ Gets a read on the current position of the car"""
        return f"({self.pos[0]},{self.pos[1]})"

    def range(self):
        """ Calculates how far you can go """
        return round(10 * (self.fuel / self.consumption), 2)

    def distance(self, target):
        """ Calculates distance between your current position and a new one """
        return math.sqrt((self.pos[0] - target[0]) ** 2 + (self.pos[1] - target[1]) ** 2)


def main():
    """ Main program """

    while True:
        print("""You've now got control of a Truck.
Type \"start\" to start the engine.""")
        car_one = Cars(colour="Red", chassis="Truck", torque="426", consumption=2.2)
        run = input("")
        while run in "start":
            car_one.start()
            loqx = input("\nWhere would you like to drive? (answer q to quit\
, answer g for fuel)\nX: ")
            if loqx == "q":
                break
            elif loqx == "g":
                print(f"{round(car_one.fuel, 2)} litres")
            else:
                loqy = float(input("Y: "))
                drive(car_one, [int(loqx), loqy])
                print(f"You're positioned at {car_one.read_position()}")
        else:
            print("Invalid option.\n--------------")

def drive(car, target):
    if not car.drive([target[0], target[1]]):
        if not car.running:
            print("Car is not running.")
        elif car.range() < car.distance(target):
            print("You don't have enough gas to make this trip.")
            # TODO: Ask if user wants to drive until fuel is empty

main()
