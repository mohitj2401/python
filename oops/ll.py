class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.next = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.next = new_node
        self.length = 2

    def prepend(self, value):
        pass

    def insert(self, value):
        pass


my_linked_lsit = LinkedList(4)
my_linked_lsit.append(5)
print(my_linked_lsit.next.value)
