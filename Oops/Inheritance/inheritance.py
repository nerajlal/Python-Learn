class Animal:

    def __init__(self):
        print("Animal Contructor")
    def eat(self):
        print("Animal is eating")
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")
    def sound(self):
        super().sound()
        print("Dog Sound")
    def bark(self):
        print("Barking")

class Puppy(Dog):
    def eat(self):
        print("Puppy Eat")

p= Puppy()
p.eat()