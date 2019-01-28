""" app
requisites: mathemathics.py, circle.py, rectangle.py
This app will combine functionality from the three modules above.
Simple command line interaction to perform simple calculations.
"""
import mathematics
import rectangle
import circle


def run_again():
    """Ask the user if running the application once more is desirable"""
    while True:
        print("--------------")
        again = input("Would you like to run again? y/n ")
        if again in ("yes", "y"):
            break
        elif again in ("n", "no"):
            exit()
        else:
            print("Non-valid answer")


while True:
    try:
        # Main menu
        print("\n----------")
        print("-- Menu --")
        print("----------\n")
        print("1 (+ - / *)")
        print("2 (rectangle area & circumference)")
        print("3 (circle area & circumference")

        CHOICE = int(input("Select an alternative:"))
        if CHOICE > 3 or CHOICE < 1:
            print("Invalid input, please select 1, 2 or 3")
        else:

            if CHOICE == 1:
                # Initiates mathematics module calculations
                print("\nYou will now enter two numbers where \nthe sum, \
difference, product and quotient will be calculated.")
                NUM1 = input("First number: ")
                NUM2 = input("Second number: ")
                print(f"The sum is {mathematics.add(NUM1, NUM2)}")
                print(f"The difference is {mathematics.sub(NUM1, NUM2)}")
                print(f"The product is {mathematics.mul(NUM1, NUM2)}")
                print(f"The quotient is {mathematics.div(NUM1, NUM2)}")
                run_again()

            elif CHOICE == 2:
                # Initiates rectangle module calculations
                print("\nYou will now enter two numbers declaring\nthe width and \
height of a rectangle of which\nthe area and circumference will \
be calculated.")
                NUM1 = input("Enter number X: ")
                NUM2 = input("Enter number Y: ")
                print(f"The area is {rectangle.area(NUM1, NUM2)}")
                print(f"The circumference is {rectangle.circ(NUM1, NUM2)}")
                run_again()

            elif CHOICE == 3:
                # Initiates circle module calculations
                print("\nYou will now enter a number declaring\nthe radius and \
of a circle of which\nthe area and circumference will \
be calculated.")
                NUM1 = int(input("Enter radius: "))
                print(f"The area is {circle.area(NUM1)}")
                print(f"The circumference is {circle.circ(NUM1)}")
                run_again()
    # If user entered string item in main menu
    except Exception:
        print("Invalid input, please select 1, 2 or 3")
