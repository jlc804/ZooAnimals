class ZooAnimals:
        """
        Class for Zoo Animals
        :params:
            self.animalType - Animal type that starts with 'S'
            self.idTag:int - Animal ID tag
            self.minTemperature:float - minimum temperatures for animal's enclosure (in Celsius)
            self.maxTemperature:float - maximum temperatures for animal's enclosure (in Celsius)
        """
    def __init__(self):
        self.animalType = coyote
        self.idTag = None
        self.minTemperature = 20
        self.maxTemperature = 100

    def __str__(self):
        return 'test'

    def getAnimalType(self):
        return self.animalType

    def getIdTag(self):
        return self.idTag

    def setIdTag(self, anIdTag):
        self.idTag = anIdTag
        return self.idTag

    def getMinTemperature(self):
        return self.minTemperature

    def getMaxTemperature(self):
        return self.maxTemperature

coyote = ZooAnimals('Coyote',25,12,12)

print(coyote.getAnimalType())
print(coyote.getIdTag())
coyote.setIdTag(100)
print(coyote.getIdTag())
print(coyote)