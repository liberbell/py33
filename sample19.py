class Character:
    def __init__(self, name):
        self.name = name

    def show_profile(self):
        profile = 'name:{0} type:Character'.format(self.name)
        print(profile)

class Monster(Character):
    def show_profile(self):
        profile = 'name:{0} type:Monster'.format(self.name)
        print(profile)

char_a = Character('CHAR A')
print(char_a.name)

monster_a = Monster('Nonster A')
print(monster_a.name)
monster_a.show_profile()