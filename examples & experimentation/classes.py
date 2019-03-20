"""
This program is the real deal ya'll
classes.py
"""


class Cars:
    """ This car class allows the creation of an endless amount of vehicles """
    def __init__(self, colour="Bare", chassis="Sedan", torque="Unspecified"):
        """ Assigns the car with factory settings """
        self.colour = colour
        self.chassis = chassis
        self.torque = int(torque)
        self.running = False
        self.xpos = 0
        self.ypos = 0

    def __str__(self):
        """ What gets printed when you print an object from this class """
        return f"Colour: {self.colour} ; Type: {self.chassis} ; Torque: {self.torque} ; \
Running: {self.running} ; Position: ({self.xpos},{self.ypos})"

    def start(self):
        """ Starts the engine """
        self.running = True

    def stop(self):
        """ Stops the engine """
        self.running = False

    def drive(self, xpos, ypos):
        """ Moves the car to a coordinate"""
        if self.running:
            self.xpos = xpos
            self.ypos = ypos
        return self.running

    def read_position(self):
        """ Gets a read on the current position of the car"""
        return f"({self.xpos},{self.ypos})"


def main():
    """ Main program """
    car_one = Cars(colour="Red", chassis="Truck", torque="216")
    car_one.start()
    print(car_one.read_position())
    if not car_one.drive(5, 2):
        print("Engine needs to be running.")

    print(car_one.read_position())
    print(car_one)


main()
