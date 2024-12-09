# A class to represent a Node with a data and next attribute
class Node:
    def __init__(self, data):
        if not isinstance(data, int):  
            raise ValueError("Node data must be an integer")
        self.data = data
        self.next = None

# A class to represent a linked list 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# Add a new node to the tail of the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

# Prints the nodes in a list, None if there is no nodes
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Reverses the linked list 
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


