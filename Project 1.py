def main():
    coyote1 = Coyote()
    coyote2 = Coyote()
    coyote3 = Coyote()
    giraffe1 = Giraffe()
    giraffe2 = Giraffe()
    giraffe3 = Giraffe()
    zoo = [coyote1, coyote2, coyote3, giraffe1, giraffe2, giraffe3]
    coyote1.setIdTag(100)
    coyote2.setIdTag(101)
    coyote3.setIdTag(102)
    giraffe1.setIdTag(200)
    giraffe2.setIdTag(201)
    giraffe3.setIdTag(202)
    User_Input = input('Input a ID Tag: ')
    while True:
        for animal in zoo:
            if str(animal.idTag) == User_Input:
                print('Animal Type: ', animal.getAnimalType())
                print('ID Tag: ', animal.getIdTag())
                print('Min Temp: ', animal.getMinTemperature())
                print('Max Temp: ', animal.getMaxTemperature())
                User_Input = input('Input a ID Tag:  ')
                continue
        if User_Input == 'X':
            break
        else:
            print('Invalid ID Tag')
            User_Input = input('Please input valid ID Tag or X to exit: ')










class Coyote:
    """Class for Coyote"""

    def __init__(self):
        self.animalType = 'Coyote'
        self.idTag = None
        self.minTemperature = 0
        # Should be in Celsius
        self.maxTemperature = 40
        #Should be in Celsius

    def getAnimalType(self):
        """Return animal type"""
        return self.animalType

    def getIdTag(self):
        """Return ID Tag"""
        return self.idTag

    def setIdTag(self, anIdTag):
        """Sets ID Tag"""
        self.idTag = anIdTag
        return self.idTag

    def getMinTemperature(self):
        """Returns Minimum Temperature in Celsius"""
        return self.minTemperature

    def getMaxTemperature(self):
        """Returns Minimum Temperature in Celsius"""
        return self.maxTemperature


class Giraffe:

    def __init__(self):
        self.animalType = "Giraffe"
        self.idTag = None
        self.minTemperature = 60
        self.maxTemperature = 95

    def getAnimalType(self):
        return self.animalType

    def getIdTag(self):
        return self.idTag

    def setIdTag(self, newIdTag):
        self.idTag = newIdTag

    def getMinTemperature(self):
        return self.minTemperature

    def getMaxTemperature(self):
        return self.maxTemperature

if __name__ == "__main__":
    main()
