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