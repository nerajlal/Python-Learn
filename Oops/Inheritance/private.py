class Parent:
    def __init__(self):
        self.__secret = "Hidden"
    def get_secret(self):
        return self.__secret

class Child(Parent):
    def show(self):
        print(self.__secret)


p = Child()
print(p.get_secret())