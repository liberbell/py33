# class A:
#     def __init__(self):
#         self.count = 1

#     def __len__(self):
#         return 10

#     def __iter__(self):
#         return self

#     def __next__(self):
#         current = self.count
#         if current > 10:
#             raise StopIteration
#         self.count += 1
#         return current

# a = A()
# # print(len(a)
# for count in a:
#     print(count)

# class A:
#     def __getitem__(self, key):
#         return key

# a = A()
# print(a[0])

class A:
    def __init__(self):
        self.name = 'type1'

    def __str__(self):
        return self.name

a = A()
print(a)