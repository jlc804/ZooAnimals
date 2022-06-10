import random

import Project3 as pokemon

class PokeGame:
    game_master = []
    def __int__(self):
        self.setup()

    def setup(self):
        p1 = pokemon.Psychic('Abra', 'Trey', 30)
        p1 = pokemon.Psychic('Gengar', 'Trey', 100)
        p2 = pokemon.Bug('Butterfree', 'Trey', 100)
        p3 = pokemon.Psychic('Kadabra', 'Trey', 50)
        p4 = pokemon.Psychic('Ghastly', 'Trey', 40)
        p5 = pokemon.Bug('Caterpie', 'Trey', 30)
        p6 = pokemon.Psychic('Mew', 'Trey', 100)
        p7 = pokemon.Bug('Metapod', 'Trey', 50)
        self.game_master = [p1,p2,p3,p4,p5,p6,p7]




    def drawPokemon(self):
        if self.game_master != []:
            return self.game_master.pop(random.randrange(len(self.game_master)))
        else:
            print('Game Over')

def main():
    game = PokeGame()
    game.setup()
    user = game.drawPokemon()
    print('Welcome to the PokeGame!')
    print('You have the following Pokemon')
    print(user)
    type_of_pokemon = int(input("Please select an available Pokemon type to battle using 1 or 2: \n1: Bug\n2: Psychic\n"))
    opp_name = input('\nPlease enter the name of the Pokemon:   ')
    opp_hp = int(input('\nPlease enter the HP:   '))
    if type_of_pokemon == 1:
        opponent = pokemon.Psychic(opp_name, 'opponent', opp_hp)
    elif type_of_pokemon == 2:
        opponent = pokemon.Bug(opp_name, 'opponent', opp_hp)
    else:
        print('Invalid Data')

    print(opponent.hp)
    while opponent.hp > 0:
        user.attack(opponent)
        print(opponent.name + ' is down to '+ str(opponent.hp))



if __name__ == "__main__":
    main()








