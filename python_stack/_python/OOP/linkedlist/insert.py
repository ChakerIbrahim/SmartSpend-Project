class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current = self.head

        while current.next != None:
            current = current.next

        current.next = new_node

    def print_list(self):
        current = self.head

        while current != None:
            print(current.data)
            current = current.next


# Create linked list
my_list = LinkedList()

my_list.add(10)
my_list.add(20)
my_list.add(30)

my_list.print_list()