# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"The {self.make} {self.model} is now starting.")

my_car = Car("Toyota", "Camry")
my_car.start()

# This creates a class Car with two instance variables make and model and a method 'start' that prints a message indicating that the car is stating.
# An instance of the class is created using my_car = Car("Toyota", "Camry"), and the method is called using my_car.start(). The output of the code would be: The Toyota Camry is now starting.