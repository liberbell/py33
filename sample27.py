# with open('hello.txt', 'x', encoding='utf-8') as file:
#     file.write('hello')

try:
    file = open('hello.txt', 'x', encoding='utf-8')
except FileExistsError:
    print('File is already exist.')
else:
    file.write('hello')
# finally:
#     file.close()