# class A:
#     def __init__(self):
#         self.__value = 1

# a = A()
# print(a._A__value)

class A:
    def __init__(self):
        self.value = 1

class B(A):
    def __init__(self, name):
        super().__init__()
        self.name = name

class C(B):
    def __init__(self, name):
        super().__init__(name)
        self.value = 10