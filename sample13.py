def hello(text, name='nemo'):
    print(text, name)

hello('bye')

def somehello(*args, **kwargs):
    print(args, kwargs)

somehello()
somehello('hi', a=1)
somehello('hi', 'hello', a=1, b=2, c=3)