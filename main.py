class ZooAnimals:
    pass

zebra = ZooAnimals()
coyote = ZooAnimals

print(zebra, coyote)

zebra.weight=10
zebra.height=12
zebra.volume=zebra.weight*zebra.height

print(str(zebra.volume))
