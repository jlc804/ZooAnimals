nd_1 = Node("11 Comae Berenices b", 1.29, 326, "2007", 1.08)
nd_2 = Node("11 Ursae Minoris b", 1.53, 1.4, "2009", 14.74)
nd_3 = Node("14 Andromedae b", 0.83, 185.8, "2008", 4.8)
nd_4 = Node("2M0437 b", 118, 3110.6, "2021", 4.0)
nd_5 = Node("30 Arietis B", 0.99, 335.1, "2009", 13.82)

node_bank[0] = Node('Epsilon Coronae Borealis b', 1.3, 417.9, 2012, 6.7)
node_bank[1] = Node('14 Andromedae b', 0.83, 185.8, 2008, 4.8)
node_bank[2] = Node('42 Draconis b', 1.19, 479.1, 2008, 3.88)
node_bank[3] = Node('COCONUTS-2 b', 7506.0, 402000013.5, 2021, 6.3)
node_bank[4] = Node('Alpha Tauri b', 1.46, 620.5, 2015, 6.47)

# A complete working Python program to
# find the length of a Linked List
# recursively

# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        # Assign data
        self.data = data

        # Initialize next as null
        self.next = None

    # Linked List class contains a Node object


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function is in LinkedList class.
    # It inserts a new node at the beginning
    # of Linked List.
    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to the new Node
        self.head = new_node

    # This function counts number of nodes in
    # Linked List recursively, given 'node'
    # as starting node.
    def getCountRec(self, node):

        # Base case
        if (not node):
            return 0
        else:
            return 1 + self.getCountRec(node.next)

    # A wrapper over getCountRec()
    def getCount(self):
        return self.getCountRec(self.head)
        # Code execution starts here


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print("Count of nodes is :",
          llist.getCount())