def hello(text, name='nemo'):
    print(text, name)

hello('bye')

def somehello(*args):
    print(args)

somehello('hi')
somehello('hi', 'hello')