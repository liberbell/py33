class A():
    def __init__(self):
        self.number = 10

class B():
    number = 10

a = A()
print(a.number)

b = B()
print(b.number)