class A():
    def __init__(self):
        self.number = 10

class B():
    number = 10

# a = A()
# print(a.number)

# b = B()
# print(b.number)

# print(B.number)
# print(A.number)

# a = A()
# a2 = A()
# print(a.number)
# print(a2.number)

b1 = B()
b2 = B()
b1.number = 5
print(b1.number)
print(b2.number)