numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squares = [num**2 for num in numbers]
print(squares)

words = ['python', 'django', 'tkinter']
upper_words = [word.upper() for word in words]
print(upper_words)

one_word = [char for word in words for char in word]
print(one_word)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in range(1, 11) if x % 2 == 1]
print(odd_numbers)

table = [[x*y for x in range(1, 10)] for y in range(1, 10)]
print(table)