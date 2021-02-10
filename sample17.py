def func():
    pass

def my_sort(string):
    return string[-1]

def price_sort(tpl):
    return tpl[1]

my_list = ['python', 'django', 'tkinter', 'requests', 'kivy']
my_list.sort(key=my_sort)
print(my_list)

print(my_sort(my_list))

my_lists = [('beans', 30), ('coffee', 12), ('chicken', 45), ('potate', 2)]
my_lists.sort()
print(my_lists)
my_lists.sort(key=lambda tpl:tpl[1])
print(my_lists)

numbers = [1, 2, 3, 4, 5]
for num in map(lambda num:num**2, numbers):
    print(num)

for num in filter(lambda num:num%2 == 0, numbers):
    print(num)