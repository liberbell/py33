my_tuple = ()
my_tuple = tuple()
print(type(my_tuple))

my_tuple = (1, True, False, 'hello')
print(type(my_tuple))
my_tuple = 1, True, False, 'hello'
print(type(my_tuple))
print(my_tuple)

one_tuple = 'hello'
print(type(one_tuple))
one_tuple = 'hello',
print(type(one_tuple))

my_tuple = 'python', 'PHP', 'Ruby', 'Perl'
print(my_tuple[0])
print(my_tuple[1:])

# my_tuple[0] = 'C++'
my_tuple.append('c')