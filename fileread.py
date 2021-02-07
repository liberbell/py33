# file = open('hello.txt', 'r', encoding='utf-8')
# src = file.read()
# print(src)
# file.close()

# with open('hello.txt', 'r', encoding='utf-8') as file:
#     src = file.read()
#     print(src)

# with open('hello.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')
#         print(type(line))

text = '''Hello
Goody
Eveny'''

with open('hello3.txt', 'w', encoding='cp932') as file:
    file.write(text)

with open('hello3.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
        print(type(line))