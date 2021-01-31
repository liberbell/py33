my_list = [1, 2, 3, 4, 5]
print(my_list)

score = {'math': 80, 'science': 50}
print(type(score))
print(score)
print(score['math'])

names = [['Bob', 'Mary'], ['Jeff', 'Beck']]
name_dict = dict(names)
print(name_dict)
print(type(name_dict))

a =['ab', 'cd', 'ef']
print(dict(a))

score = {}
score['math'] = 80
print(score)
print(type(score))

score = {}
science = score.get('science', 'no data')
print(science)
score['science'] = 100
science = score.get('science', 'no data')
print(science)

math = score.get('math')
print(math)
print(type(None))

band_members = {'guiter': 'Jeff', 'drum': 'Jhon'}
new_members = {'Piano': 'Elton', 'Vocal':'Eric'}

band_members.update(new_members)
print(band_members)
print(new_members)

band_members = {'guiter': 'Jeff', 'drum': 'Jhon'}
new_members = {'drum': 'Steven'}
band_members.update(new_members)
print(band_members)

deleted = band_members.pop('guiter')
print(deleted)
print(band_members)
print('drum' in band_members)

drum = band_members.setdefault('drum', 'Aaron')
print(drum)
guiter = band_members.setdefault('guiter', 'Jeff')
print(guiter)

print(band_members.keys())
print(band_members.values())