from Pokemon_Class import Psychic as Psychic
from Pokemon_Class import Bug as Bug
import random
class PokeGame:
    game_master = []
    def __int__(self):
        self.setup()

    def setup(self):
        p1 = Psychic('Abra', 'Trey', 30)
        p1 = Psychic('Gengar', 'Trey', 100)
        p2 = Bug('Butterfree', 'Trey', 100)
        p3 = Psychic('Kadabra', 'Trey', 50)
        p4 = Psychic('Ghastly', 'Trey', 40)
        p5 = Bug('Caterpie', 'Trey', 30)
        p6 = Psychic('Mew', 'Trey', 100)
        p7 = Bug('Metapod', 'Trey', 50)
        self.game_master = [p1,p2,p3,p4,p5,p6,p7]
        #return self.game_master

    def drawPokemon(self):
        if self.game_master != []:
            return self.game_master.pop(random.randrange(len(self.game_master)))
        else:
            print('Game Over')





