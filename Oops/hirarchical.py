class Animal:
    def sound1(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")


d = Dog()
d.sound1()