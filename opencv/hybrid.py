
class A:
    def display(self):
        print("hello")

class B(A):
    def show1(self):
        print("Hey")

class C:
    def show2(self):
        print("Yooooo")

class D(B,C):
    def display1(self):
        print("final")

d1 = D()
d1.display1()
d1.show1()
d1.show2()
d1.display()