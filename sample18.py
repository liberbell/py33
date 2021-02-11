# print(type(1))
# print(type('char'))
# print(type([1]))

# members = {}

# def add_score(name, point):
#     members[name] = point

# def get_score(name):
#     return members.get(name, 'nobody')

# add_score('Bob', 50)
# Bob_score = get_score('Bob')
# print(Bob_score)

# members = {}

# def add_score(name, subject, point):
#     student = members.setdefault(name, {})
#     student[subject] = point

# def get_score(name, subject):
#     student = members.get(name)
#     if not student:
#         return 'nobody'
#     point = student.get(subject)
#     if not point:
#         return 'not yet the subject'
#     return point

# add_score('Bob', 'science', 88)
# Bob_science = get_score('Bob', 'math')
# print(Bob_science)

members = {}

class Student:
    def __init__(self, name):
        self.name = name
        self.score = {}

    def add_score(self, subject_name, point):
        self.score[subject_name] = point

    def get_score(self, subject_name):
        return self.score.get(subject_name, 'not yet')

Bob = Student('Bob')
Bob.add_score('science', 82)
print(Bob.score)

Eric = Student('Eric')
Eric.add_score('science', 40)
print(Eric.score)
