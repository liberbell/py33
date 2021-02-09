def func():
    pass

def my_sort(string):
    return string[-1]

my_list = ['python', 'django', 'tkinter', 'requests', 'kivy']
my_list.sort(key=my_sort)
print(my_list)

print(my_sort(my_list))

my_lists = [('beans', 30), ('coffee', 12), ('chicken', 45), ('potate', 2)]
my_lists.sort()
print(my_lists)