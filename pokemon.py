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
                other.receive_damage(self.damage*2)
            elif other.type in self.weak_against:
                other.receive_damage(self.damage/2)
            else:
                other.receive_damage(self.damage)
        if random() < self.prob:
            other.status_condition = 'confused'
            print(other.name + ' is ' + other.status_condition)

    def __str__(self):
        return super().__str__() + " HP " + str(self.hp)

