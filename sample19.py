class Character:
    def __init__(self, name):
        self.name = name

    def show_profile(self):
        profile = 'name:{0} type:Character'.format(self.name)
        print(profile)

class Monster(Character):
    def __init__(self, name):
        super().__init__(name)
        # self.name = name
        self.HP = 20

    def show_profile(self):
        profile = 'name:{0} type:Monster HP:{1}'.format(self.name, self.HP)
        print(profile)

char_a = Character('CHAR A')
print(char_a.name)

monster_a = Monster('Nonster A')
print(monster_a.name)
monster_a.show_profile()
print(monster_a.HP)