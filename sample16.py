# def make_squares(n):
#     numbers = []
#     for i in range(n, n+1):
#         numbers.append(i**2)
#     return numbers

# squares = make_squares(10)
# print(squares)


# def make_squares2(n):
#     for i in range(n, n+1):
#         yield i**2

# squares = make_squares2(10)
# for i in squares:
#     print(i)

def my_range(start, end, step):
    current_number = start

    while current_number < end:
        yield current_number
        current_number += step

# print(my_range(1, 10, 2))

for i in my_range(1, 10, 2):
    print(i)