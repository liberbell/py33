fmt = 'My name is {}.'
name = 'ted'

print(fmt.format(name))
print(fmt.format('bob'))

fmt = 'My name is {} {}.'
print(fmt.format('jake', 'Calen'))

fmt = '{0} {1} {0}'
print(fmt.format('a1', 'a2'))