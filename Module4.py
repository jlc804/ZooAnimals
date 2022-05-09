# Node class
class PlanetNode:

    def __init__(self, ID, radius, period, discovery, mass, next=None):
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
        return totalmass


def main():
    list = PlanetList()
    list.push("11 Comae Berenices b", 1.29, 326, 2007, 1.08)
    list.push('COCONUTS-2 b', 7506.0, 402000013.5, 2021, 6.3)
    list.push("11 Comae Berenices b", 1.29, 326, 2007, 1.08)
    list.push("11 Ursae Minoris b", 1.53, 1.4, 2009, 14.74)
    list.push('14 Andromedae b', 0.83, 185.8, 2008, 4.8)
    list.push('42 Draconis b', 1.19, 479.1, 2008, 3.88)
    print(list.getMass())









if __name__ == '__main__':
    main()

