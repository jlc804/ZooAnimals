from Pokemon_Class import Psychic as Psychic
from Pokemon_Class import Bug as Bug

def main():
    from PokeGame import PokeGame as PokeGame
    from Pokemon_Class import Pokemon as pokemon
    game = PokeGame()
    game.setup()
    opponent = game.drawPokemon()
    print('Welcome to the PokeGame!')
    print('The following Pokemon is available to battle')
    print(opponent)
    type_of_pokemon = int(input("Please select an available Pokemon type to battle using 1 or 2: \n1: Bug\n2: Psychic\n"))
    user_pokename = input('\nPlease enter the name of the Pokemon:   ')
    user_hp = int(input('\nPlease enter the HP:   '))
    print(user_hp)
    if type_of_pokemon == 1:
        user = Bug(user_pokename, 'user', user_hp)
        print(user)

    elif type_of_pokemon == 2:
        user = Psychic(user_pokename, 'user', user_hp)
    else:
        print('Invalid Data')


    print(opponent.hp)
    while opponent.hp > 0:
        user.attack(opponent)
        print(opponent.name + ' is down to '+ str(opponent.hp))




if __name__ == "__main__":
    main()