def create_int_list(numbers=[]):
    for i in range(10):
        numbers.append(i)
    return numbers

numbers = create_int_list()
print(numbers)

numbers2 = create_int_list()
print(numbers2)

numbers3 = create_int_list()
print(numbers3)

def create_int_list2(numbers=None):
    if numbers is None:
        numbers = []
    for i in range(10):
        numbers.append(i)
    return numbers

numbers = create_int_list2()
print(numbers)

numbers2 = create_int_list2()
print(numbers2)

numbers3 = create_int_list2()
print(numbers3)