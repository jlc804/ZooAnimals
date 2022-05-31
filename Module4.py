class PlanetNode:
    def __init__(self, ID, radius, period, discovery, mass, next = None):
        self.ID = ID
        self.radius = radius
        self.period = period
        self.discovery = discovery
        self.mass = mass
        self.next = next

    def total_mass(self):
        return self.mass

class PlanetList:
    def __init__(self):
        self.head = None

    def push(self, ID, radius, period, discovery, mass):
        new_node = PlanetNode(ID, radius, period, discovery, mass)
        new_node.next = self.head
        self.head = new_node

    def getMass(self):
        return self.getTotalMass(self.head)

    def getTotalMass(self, node):
        totalmass = 0
        temp = self.head
        while (temp):
            totalmass += temp.mass
            temp = temp.next
        return round(float(totalmass),6)


def main():
    planetlist = PlanetList()
    planetlist.push('30 Arietis B b', 0.99, 335.1, 2009, 13.82)
    planetlist.push('4 Ursae Majoris b', 0.87, 269.3, 2006, 7.1)
    planetlist.push('AU Microscopii b', 0.0645, 8.5, 2020, 17)
    planetlist.push('BD+03 2562 b', 1.3, 481.9 , 2017, 1.13)
    planetlist.push('CD Ceti b', 0.0185, 2.3 , 2020, 1.82)
    planetlist.push('Kepler-1012 b', 0.0585, 5.5, 2016, 2.21)
    totalmass = planetlist.getMass()
    print('The total mass of all exoplanets in the list is the equivalent of ' + str(totalmass) + ' Jupiters!' )









if __name__ == '__main__':
    main()

