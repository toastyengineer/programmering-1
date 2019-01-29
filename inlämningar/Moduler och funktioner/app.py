""" app
requisites: mathematics.py, circle.py, rectangle.py
This app will combine functionality from the three modules above.
Simple command line interaction to perform simple calculations.
"""
import mathematics
import rectangle
import circle


def run_again():
    """Ask the user if running the application once more is desirable"""
    while True:
        again = input("Would you like to run again? y/n ")
        if again in ("yes", "y"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            return True
        elif again in ("n", "no"):
            return False
        print("Invalid answer")


while True:
    # Print the main menu
    print("""
            ----------
          **** Menu ****
            ----------""")
    print("""
What would you like to do?
1: (+ - / *)
2: (Rectangle Area & Circumference
3: (Circle Area & Circumference
        """)
    try:  # Selector for what you want to do
        CHOICE = int(input("Select an alternative: "))
        if CHOICE > 3 or CHOICE < 1:
            print("\n\n\n\n\n\n\n\n\n\n\n\nInvalid input, please select 1, 2 or 3\n\n")
        else:

            if CHOICE == 1:
                # Initiates mathematics module calculations
                print("""----------
You will now enter two numbers from which the sum,
difference, product and quotient will be calculated.
----------""")
                NUM1 = input("First number: ")
                NUM2 = input("Second number: ")
                print(f"""----------
The sum is {mathematics.add(NUM1, NUM2)}
The difference is {mathematics.sub(NUM1, NUM2)}
The product is {mathematics.mul(NUM1, NUM2)}
The quotient is {mathematics.div(NUM1, NUM2)}
----------""")
                if not run_again():
                    exit(0)

            elif CHOICE == 2:
                # Initiates rectangle module calculations
                print("""----------
You will now enter two numbers declaring the width
and height of a rectangle from which the area
and circumference will be calculated.
----------""")
                NUM1 = input("Enter number X: ")
                NUM2 = input("Enter number Y: ")
                print(f"""----------
The area is {rectangle.area(NUM1, NUM2)}
The circumference is {rectangle.circ(NUM1, NUM2)}
----------""")
                if not run_again():
                    exit(0)

            elif CHOICE == 3:
                # Initiates circle module calculations
                print("""----------
You will now enter a number declaring the radius
of a circle from which the area and circumference
will be calculated.
----------""")
                NUM1 = input("Enter radius: ")
                print(f"""----------
The area is {circle.area(NUM1)}
The circumference is {circle.circ(NUM1)}
----------""")
                if not run_again():
                    exit(0)
    except ValueError:  # If user entered string item in main menu
        print("\n\n\n\n\n\n\n\n\n\n\n\nInvalid input, please select 1, 2 or 3\n\n")
