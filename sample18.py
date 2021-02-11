print(type(1))
print(type('char'))
print(type([1]))

members = {}

def add_score(name, point):
    members[name] = point

def get_score(name):
    return members.get(name, 'nobody')

add_score('Bob', 50)
Bob_score = get_score('Bob')
print(Bob_score)