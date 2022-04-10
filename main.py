class Coyote:
    """Class for Coyote"""

    def __init__(self):
        self.animalType = 'coyote'
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

coyote = Coyote()
print(coyote.getAnimalType())
print(coyote.getIdTag())
coyote.setIdTag(100)
print(coyote.getIdTag())
print(coyote.getMinTemperature())
print(coyote.getMaxTemperature())