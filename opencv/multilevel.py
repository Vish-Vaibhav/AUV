# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Labrador(Dog):
    def color(self):
        print("Labrador is brown")

labrador_obj = Labrador()

labrador_obj.speak() 
labrador_obj.bark()
labrador_obj.color()
