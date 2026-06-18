class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class SingLe_linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # insert (At_head,At_tail,position)
    # create new node
    # new node point to head
    # new node will be the head
    def insert_at_head(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    # create node(manually)
    # first = Node(100)
    # Second = Node(200)
    # third = Node(300)
    # fourth = Node(400)

    # first.next = Second
    # Second.next = third
    # third.next = fourth

    def insert_at_tail(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.tail = new_node
        return self.head

    def traverse(self):
        Current = self.head
        while Current is not None:
            print(Current.value, end="=>")
            Current = Current.next
        print("Null")

    # SLL = SingLe_linkedList()
    # SLL.insert_at_tail(100)
    # SLL.insert_at_tail(200)
    # SLL.insert_at_tail(300)
    # SLL.insert_at_tail(400)
    # SLL.insert_at_head(5000)
    # SLL.traverse()
    def insert_index(self, val, position):
        new_node = Node(val)
        current = self.head
        for i in range(position - 1):
            current = current.next

        temp = current.next
        new_node.next = temp
        current.next = new_node


SLL = SingLe_linkedList()
SLL.insert_at_tail(100)
SLL.insert_at_tail(200)
SLL.insert_at_tail(300)
SLL.insert_at_tail(400)
SLL.insert_at_head(5000)
SLL.insert_index(3000, 3)
SLL.traverse()
