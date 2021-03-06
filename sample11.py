my_set = {1, 2, 3}
print(my_set)
print(type(my_set))

my_set = set()
my_list = [1, 2, 3]
my_set = set(my_list)
print(my_set)
print(type(my_set))

my_list = [1, 2, 4, 4, 3, 5, 2, 8, 9, 1]
print(my_list)

my_set = set(my_list)
print(my_set)

mutable = {'list', 'dict', 'set'}
imutable = {'str', 'number', 'tuple'}
seq = {'list', 'tuple', 'str'}

print(mutable & seq)
print(mutable.intersection(seq))
print(mutable | seq)
print(imutable - seq)
print(mutable ^ seq)