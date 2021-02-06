# text = '''good morning
# hello
# good evening'''

test = 'added'

file = open('hello.txt', 'a', encoding='utf-8')
file.write(text)
file.close()