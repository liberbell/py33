# while True:
#     user_input = input()
#     if user_input == 'exit':
#         break
#     elif user_input == 'skip':
#         continue
#     else:
#         print('input: ', user_input)

names = ['JamesBrown', 'EltonJohn', 'JeffBeck']
is_found = False
for name in names:
    if name.endswith('John'):
        is_found = True

if is_found == True:
    print('We found!')
else:
    print('no body there.')