def create_int_list(numbers=[]):
    for i in range(10):
        numbers.append(i)
    return numbers

numbers = create_int_list()
print(numbers)