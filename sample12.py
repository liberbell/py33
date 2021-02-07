def hello():
    print('say hello')

hello()

def helloto(name):
    message = 'Mr.{0}, hello.'.format(name)
    print(message)

helloto('Been')

def check_name(name):
    if len(name) >= 6:
        return True
    else:
        return False

name= input('name?',)
print(check_name(name))