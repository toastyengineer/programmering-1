class Dog:

    def __init__(self, race=''):
        self.race = race

    def bark(self):
        print("Voff voff")


if __name__ == "__main__":
    my_dog = Dog('Doberman')
    your_dog = Dog('Poodle')
    my_dog.bark()
