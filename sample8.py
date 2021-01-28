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