numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))

numbers.insert(1, 1.5)
print(numbers)

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers1.extend(numbers2)
print(numbers1)

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = numbers1 + numbers2
print(numbers3)

numbers = [1, 2, 3, 4, 5]
numbers.pop(0)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.pop())

my_list = ['a', 'i', 'u']
my_list.remove('i')
print(my_list)

numbers = [1, 2, 3]
print(numbers.index(2))
print(1 in numbers)
print(100 in  numbers)

numbers = [1, 1, 2, 4, 1, 2, 1, 5]
print(numbers.count(1))
print(numbers.count(8))

parts = ['It', 'is', 'fine', 'day']
poem = '\n'.join(parts)
print(poem)

numbers = [5, 1, 3, 3, 5, 2, 8, 9, 4]
numbers.sort()
print(numbers)

print('after sort')