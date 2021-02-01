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