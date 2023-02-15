class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length = self.length+1

    def pop(self):
        if (self.head == None):
            return -1
        else:
            pop_node = self.head.value
            if (self.head.next == None):
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return pop_node

    def insert(self, value):
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_lsit = LinkedList(4)
my_linked_lsit.append(5)
my_linked_lsit.append(10)

val = my_linked_lsit.pop()
print(val)
print("-----------------------------------")
val = my_linked_lsit.pop()
print(val)
print("-----------------------------------")

my_linked_lsit.print_list()
print("-----------------------------------")

val = my_linked_lsit.pop()
print(val)
print("-----------------------------------")

my_linked_lsit.print_list()
my_linked_lsit.append(5)
print("-----------------------------------")

val = my_linked_lsit.pop()
print(val)
print("-----------------------------------")

my_linked_lsit.print_list()
print("-----------------------------------")

my_linked_lsit.append(10)
my_linked_lsit.print_list()
print("-----------------------------------")

val = my_linked_lsit.pop()
print(val)
print("-----------------------------------")

val = my_linked_lsit.pop()
print(val)
print("-----------------------------------")
