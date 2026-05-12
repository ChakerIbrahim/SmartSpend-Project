class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
first = Node(1)
second = Node(2)
third = Node(3)

# Connect nodes
first.next = second
second.next = third

# Traverse list
current = first

while current != None:
    print(current.data)
    current = current.next