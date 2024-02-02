# inheritance in simple terms is the ability to define a new class that is a modified version of an existing class.
# Inheritance is a powerful feature in object-oriented programming.
# It allows a class to inherit attributes and methods from another class.

# example of inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    # Fish class inherits from Animal class
    def __init__(self):
        super().__init__()  # call the __init__ method of the parent class and inherit the attributes and methods

    def breathe(self):
        super().breathe() # call the breathe method of the parent class then add more functionality
        print("doing this underwater")

    def swim(self):
        print("moving in water")


neo = Fish()
neo.swim()
neo.breathe()
