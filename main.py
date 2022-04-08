class ZooAnimals:
    def __init__(self, weight, height):
        self.x = weight
        self.height = height
        self.volume = weight * height
        self.whatever = 0

    def fullname(self):
        return self.whatever

    def __str__(self):
        return '45'

zebra = ZooAnimals(10,12)
coyote = ZooAnimals(15,25)

print(zebra.x, coyote.volume)
print(zebra.fullname())

print(ZooAnimals.fullname(zebra))
print(ZooAnimals(3,4))
