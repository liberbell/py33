# text = '''good morning
# hello
# good evening'''

text = 'added'

file = open('hello.txt', 'x', encoding='utf-8')
file.write(text)
file.close()