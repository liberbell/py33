file = open('hello.txt', 'r', encoding='utf-8')
src = file.read()
print(src)
file.close()

with open('hello.txt', 'r', encoding='utf-8') as file:
    src = file.read()
    print(src)