from random import random

class Pokemon:
    basic_attack = 'tackle'
    damage = 40;

    def __init__(self, name, trainer):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.hp = 50
        self.status_condition = None
        self.prob = None
        self.type = ''
        self.strong_against = ['Grass', 'Psychic', 'Dark']
        self.weak_against = ['Fighting', 'Flying', 'Poison', 'Ghost', 'Fire', 'Fairy']

    def __str__(self):
        return self.name + '' + self.trainer

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        if self.status_condition == None:
            self.speak()
            print(self.name, ' used ', self.basic_attack, '!')
            other.receive_damage(self.damage)

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(self.name, ' fainted!')

class TestType(Pokemon):
    def __init__(self, name, trainer, hp):
        super().__init__(name, trainer)
        self.level = 1
        self.hp = hp
        self.prob = .1
        self.type = 'Fighting'
        self.strong_against = ['Grass', 'Psychic', 'Dark']
        self.weak_against = ['Fighting', 'Flying', 'Poison', 'Ghost', 'Fire', 'Fairy']



class BugType(Pokemon):
    def __init__(self, name, trainer, hp):
        super().__init__(name, trainer)
        self.hp = hp
        self.basic_attack = 'Signal Beam'
        self.prob = .1
        self.type = 'Bug'
        self.strong_against = ['Grass', 'Psychic', 'Dark']
        self.weak_against = ['Fighting', 'Flying', 'Poison', 'Ghost', 'Fire', 'Fairy']

    def attack(self, other):
        if  self.status_condition == None:
            self.speak()
            print(self.name, 'used', self.basic_attack, '!')
            if other.type in self.strong_against:
                print('yes')
                other.receive_damage(self.damage*2)
            elif other.type in self.weak_against:
                other.receive_damage(self.damage/2)
            else:
                other.receive_damage(self.damage)
        if random() < self.prob:
            other.status_condition = 'confused'
            print(other.name + ' is ' + other.status_condition)

    def __str__(self):
        return super().__str__() + " hp" + str(self.name) + ")"




Butterfree = BugType('Butterfree', 'Trey',100)
Charizard =TestType('Char', 'Trey', 100)
print(Butterfree.hp)
Butterfree.attack(Charizard)
Charizard.attack(Butterfree)
print(Butterfree.hp)
print(Charizard.hp)

print(Butterfree)

