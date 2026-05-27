from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("UPI Payment")

class Card(Payment):
    def pay(self):
        print("Card Payment")

class Crypto(Payment):
    def pay(self):
        print("Crypto Payment")
    def check(self):
        print("Check")

payments = [UPI(), Card(), Crypto()]
for p in payments:
    p.pay()

pay = Crypto()
pay.check()
