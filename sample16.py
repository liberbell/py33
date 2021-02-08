def make_squares(n):
    numbers = []
    for i in range(n, n+1):
        numbers.append(i**2)
    return numbers

squares = make_squares(10)
print(squares)
for i in squares:
    print(i)