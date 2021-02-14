# class Person():
#     def __init__(self, name):
#         self.name = name

# person = Person('')
# print(person.name)

class Person:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            value = 'nemo'
        self._name = value