fmt = 'My name is {}.'
name = 'ted'

print(fmt.format(name))
print(fmt.format('bob'))

fmt = 'My name is {} {}.'
print(fmt.format('jake', 'Calen'))

fmt = '{0} {1} {0}'
print(fmt.format('a1', 'a2'))

last_name = 'Jake'
first_name = 'Calen'
print(f'{last_name} {first_name}')
print('My name is %s.' % last_name)

languages = 'python,PHP,Ruby,Perl'
print(languages.split(','))

# languages = 'python,php,Ruby,Perl'
lang_list = languages.split(',')
separator = ','
separator.join(lang_list)
print(separator.join(lang_list))

poem = 'It was nice day.'
new_poem = poem.replace('nice', 'bad')
print(poem)
print(new_poem)

text = 'hello, hello, helo, hello'
print(text.count('hello'))

name = 'Billy Joel'
print(name.startswith('Billy'))
print(name.startswith('Tomy'))

print(name.endswith('Joel'))
print(name.endswith('Mary'))

text = 'Good morning people'
print(text.find('morning'))

print(text.index('people'))
# print(text.index('lady'))

# print('Biily' in name)
text = '      Hello      '
print(text)
print(text.lstrip())