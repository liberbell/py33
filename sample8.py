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