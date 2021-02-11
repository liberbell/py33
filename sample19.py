class Character:
    def __init__(self, name):
        self.name = name

    def show_profile(self):
        profile = 'name:{0} type:{1}'.format(self.name)
        print(profile)

class Monster(Character):
    pass

char_a = Character('CHAR A')
print(char_a.name)

monster_a = Monster('Nonster A')
print(monster_a.name)