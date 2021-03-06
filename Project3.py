from Pokemon_Class import Psychic as Psychic
from Pokemon_Class import Bug as Bug
from PokeGame import PokeGame as PokeGame

def main():
    game = PokeGame()
    game.setup()
    opponent = game.drawPokemon()
    print('Welcome to the PokeGame!')
    print('The following Pokemon is available to battle')
    print(opponent)
    type_of_pokemon = int(input("Please select an available Pokemon type to battle using 1 or 2: \n1: Bug\n2: Psychic\n"))
    user_pokename = input('\nPlease enter the name of the Pokemon:   ')
    user_hp = int(input('\nPlease enter the HP:   '))
    if type_of_pokemon == 1:
        user = Bug(user_pokename, 'user', user_hp)
        print(user)

    elif type_of_pokemon == 2:
        user = Psychic(user_pokename, 'user', user_hp)
    else:
        print('Invalid Data')

    while opponent.hp > 0:
        user.attack(opponent)
        if opponent.hp > 0:
            print(opponent.name + ' is down to '+ str(opponent.hp) + 'HP')




if __name__ == "__main__":
    main()