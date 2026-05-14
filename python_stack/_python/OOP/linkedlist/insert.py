class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, position):
        if position < 0 or position >= self.size:
            return None

        current = self.head

        for i in range(position):
            current = current.next

        return current.value

    def addAtHead(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)
        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head

            for _ in range(index - 1):
                current = current.next

            current.next = current.next.next

        self.size -= 1


# TEST

my_list = LinkedList()

my_list.addAtHead(10)
my_list.addAtTail(30)

