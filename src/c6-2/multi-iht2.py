class A:
    def print(self):
        print("A")

class AB:
    def print(self):
        print("AB")

class AC:
    def print(self):
        print("AC")

class D1(AB, AC):
    pass

class D2(AC, AB):
    pass

obj1 = D1()
obj1.print()
obj2 = D2()
obj2.print()

