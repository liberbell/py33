your_input = input('Enter a number: ')
try:
    number = int(your_input)
    print(number)
except:
    print('Your input is string.')