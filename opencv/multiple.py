# Base class 1
class Animal:
    def speak(self):
        print("Animal speaks")

# Base class 2
class Bird:
    def fly(self):
        print("Bird can fly")

class Parrot(Animal, Bird):
    def color(self):
        print("Parrot is colorful")

parrot_obj = Parrot()

parrot_obj.speak()
parrot_obj.fly()
parrot_obj.color()
