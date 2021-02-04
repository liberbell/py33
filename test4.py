# for i in range(1, 101):
#     if i % 15 == 0:
#         print('fizz buzz', end=' ')
#     elif i % 5 == 0:
#         print('buzz', end=' ')
#     elif i % 3 == 0:
#         print('fizz', end=' ')
#     else:
#         print(i, end=' ')
# print(6 % 2)

for i in range(1, 101):
    message = ''
    if i % 3 == 0:
        message += 'Fizz'
    
    if i % 5 == 0:
        message += 'Buzz'

    if message:
        print(message, end=' ')
    else:
        print(i, end=' ')