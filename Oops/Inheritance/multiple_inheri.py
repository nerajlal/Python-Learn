class Father:
    def skill1(self):
        print("DRIVING")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()

c.skill1()