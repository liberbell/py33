result = 1 + 1
print(result)

names = ['James', 'Bob', 'Sting']
if 'James' in names:
    print('The names included.')
    if 'Bob' in names:
        print('Bob included too.')
    else:
        print('Bob is absent.')

else:
    print('The name not in list.')
    print('sorry.')
print('End of processing.')

color = 'white'
if color == 'red':
    print('Color is red.')
elif color == 'blue':
    print('Color is blue')
elif color == 'white':
    print('Color is white')
else:
    print('Color is other color.')

numbers = [1, 2, 3, 4, 5]
if 1 in numbers and 2 in numbers:
    print('1 and 2 are in the list.')
else:
    print('out of list number.')