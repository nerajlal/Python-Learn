class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} started")


class Car(Vehicle):

    def drive(self):
        print("Driving car")

class Bike(Vehicle):

    def ride(self):
        print("Riding Bike")



c = Car("BMW")

c.start()
c.drive()



b = Bike("Hero")

b.start()
b.ride()