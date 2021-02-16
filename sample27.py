# with open('hello.txt', 'x', encoding='utf-8') as file:
#     file.write('hello')

file = None
try:
    file = open('hello.txt', 'x', encoding='utf-8')
except FileExistsError:
    print('File is already exist.')
else:
    file.write('hello')
finally:
    if file is not None:
        file.close()