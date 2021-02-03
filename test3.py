# for i in range(1, 101, 2):
#     print('value is {0}'.format(i))

# my_list = list(range(1, 101))
# print(my_list)

names = ['Eric', 'Bob', 'Elton']
# index = 0
# for name in names:
#     # index = ...
#     message = '{0} is {1}th.'.format(name, index)
#     print(message)
#     index += 1


for index, name in enumerate(names):
    # index = ...
    message = '{0} is {1}th.'.format(name, index)
    print(message)

foods = ['apple', 'baked pie', 'chocolate']
drinks = ['coffee', 'beer', 'wine']

for food, drink in zip(foods, drinks):
    # print(food)
    # print(drink)
    print(food, drink)

foods = ['apple', 'baked pie', 'chocolate']
drinks = ['coffee', 'beer']

for food, drink in zip(foods, drinks):
    # print(food)
    # print(drink)
    print(food, drink)