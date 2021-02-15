your_input = input('Enter a number: ')
try:
    number = int(your_input)
    print(10 / number)
except ValueError:
    print('Your input is string.')
except ZeroDivisionError:
    print('Do not divided by zero.')
except:
    print('other error.')