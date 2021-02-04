numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squares = [num**2 for num in numbers]
print(squares)

words = ['python', 'django', 'tkinter']
upper_words = [word.upper() for word in words]
print(upper_words)

one_word = [char for word in words]
print(one_word)