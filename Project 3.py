from random import random

class Pokemon:
    basic_attack = 'tackle'
    damage = 40;

    def __init__(self, name, trainer):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.hp = 50
        self.status_condition = ''
        self.type = ''

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            print(self.name, ' used ', self.basic_attack, '!')
            other.receive_damage(self.damage)

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(self.name, ' fainted!')


class BugType(Pokemon):
    def __init__(self, name, trainer, hp):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.hp = hp
        self.status_condition = ''
        self.basic_attack = 'Signal Beam'
        self.prob = .1
        self.strong_against = ['Grass', 'Psychic', 'Dark']
        self.weak_against = ['Fighting', 'Flying', 'Poison', 'Ghost', 'Fire', 'Fairy']

    def attack(self, other):
        if  self.status_condition == None:
            self.speak()
            print(self.name, 'used', self.basic_attack, '!')
            other.receive_damage(self.damage)
        if random() < self.prob:
            other.status_condition = 'confused'
            print(other.name + ' is ' + other.status_condition)

    def __str__(self):
        pass



Butterfree = BugType('Butterfree', 'Trey',100)
Charizard =0
print(Butterfree.hp)
Butterfree.attack(Butterfree)


