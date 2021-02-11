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

class Student:
    pass

a = Student()