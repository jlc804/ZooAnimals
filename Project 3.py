from random import random


class Pokemon:
    basic_attack = 'tackle'
    damage = 40;

    def __init__(self, name, trainer):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.hp = 50
        self.paralyzed = False

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

class Psychic(Pokemon):
#Psychic Pokemon Class provided by Matthew Skokos
    def __init__(self, name, trainer, hp):
        super().__init__(name, trainer)
        self.hp = hp
        self.basic_attack = 'Psychic Shift'
        self.prob = 1.0
        self.status_condition = None

    def attack(self, other):
        if  self.status_condition != "paralyzed":
            self.speak()
            print(self.name, 'used', self.basic_attack, '!')
            if isinstance(other, (Poison, Fighting)):
                other.receive_damage(self.damage * 2)
            elif isinstance(other, (Bug, Ghost, Dark)):
                other.receive_damage(self.damage / 2)
            else:
                other.receive_damage(self.damage)

        if random() < self.prob and not isinstance(other, Psychic):
            other.status_condition = 'paralyzed'
            print(other.name + ' is ' + other.status_condition)

    def __str__(self):
        return f'I am {self.name} and I can do {self.basic_attack}'


class Bug(Pokemon):
    def __init__(self, name, trainer, hp):
        super().__init__(name, trainer)
        self.hp = hp
        self.basic_attack = 'Signal Beam'
        self.prob = .1
        self.status_condition = None

    def attack(self, other):
        if  self.status_condition is None:
            self.speak()
            print(self.name, 'used', self.basic_attack, '!')
            if isinstance(other, (Grass, Psychic, Dark)):
                other.receive_damage(self.damage*2)
            elif isinstance(other, (Fighting, Flying, Poison, Ghost,Fire,Fairy)):
                other.receive_damage(self.damage/2)
            else:
                other.receive_damage(self.damage)
        if random() < self.prob:
            other.status_condition = 'confused'
            print(other.name + ' is ' + other.status_condition)

    def __str__(self):
        return super().__str__() + " HP " + str(self.hp)


class Poison(Pokemon):
    pass
class Fighting(Pokemon):
    pass
class Ghost(Pokemon):
    pass
class Dark(Pokemon):
    pass
class Grass(Pokemon):
    pass
class Flying(Pokemon):
    pass
class Fire(Pokemon):
    pass
class Fairy(Pokemon):
    pass


Butterfree = Bug('Butterfree', 'Trey',100)


p1 = Psychic('Mewtwo', 'Jen', 100)
p2 = Psychic('Gengar', 'James', 40)

print(p1.hp)
Butterfree.attack(p2)
p2.attack(Butterfree)

print(p2.hp)
print(p1.hp)

