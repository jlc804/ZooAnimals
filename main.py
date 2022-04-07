class ZooAnimals:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.volume = weight * height


zebra = ZooAnimals(10,12)
coyote = ZooAnimals(15,25)

print(zebra.volume, coyote.volume)

