names = ['James', 'Elton', 'Eric']

for name in names:
    print(name)

# for char in 'Helloworld':
#     print(char)

# for name in names:
#     for char in name:
#         print(char)

band_members = {'vocal': 'James', 'piano': 'Elton', 'guiter': 'Eric'}
for part in band_members:
    # print(part)
    name = band_members[part]
    result = '{0} is {1}'.format(part, name)
    print(result)

for name in band_members.values():
    print(name)

for key, value in band_members.items():
    message = '{0} is {1}.'.format(key, value)
    print(message)

my_tuple = (1, 2)
a, b = my_tuple
print(a, b)