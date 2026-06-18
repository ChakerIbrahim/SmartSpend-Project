class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Create nodes manually
first = Node(10)
second = Node(20)
third = Node(30)

# Connect nodes
first.next = second
second.next = third

# Traverse list
current = first

while current != None:
    print(current.value,end ="->")
    current = current.next
print("Null")

class LinkedList:
    def __init__(self):
        self.head = None

# my_list = LinkedList()
# my_list.head = first
# first.next = second
# print(my_list.head.value)
# print(my_list.head.next.value)

    def addAtHead(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node 
        return self
# my_list = LinkedList()
# my_list.addAtHead(10).addAtHead(20).addAtHead(30).addAtHead(40)
# current = my_list.head
# while current:
#     print(current.value,end = '->')
#     current = current.next
# print("NULL")

    def addAtTail(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        return self
# my_list = LinkedList()
# my_list.addAtTail(50).addAtTail(40).addAtTail(30)
# current = my_list.head
# while current:
#     print(current.value,end = '->')
#     current = current.next

    def delete(self,position):
        current = self.head
        for i in range(position-1):
            current = current.next
        current.next = current.next.next
        return self

# my_list = LinkedList()
# my_list.addAtTail(10).addAtTail(20).addAtTail(30).addAtTail(40)
# my_list.delete(2)
# current = my_list.head
# while current:
#     print(current.value, end=" -> ")
#     current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        return self
# my_list = LinkedList()
# my_list.addAtTail(30).addAtTail(20).addAtTail(10)
# my_list.reverse()
# current = my_list.head
# while current:
#     print(current.value, end=" -> ")
#     current = current.next     

    def addindex(self,val,index):
        if index == 0:
            New_node.next =self.head
            self.head = New_node
        
        New_node = Node(val)
        current = self.head
        for i in range(index-1):
            current = current.next 
        New_node.next = current.next
        current.next = New_node
        

my_list = LinkedList()
my_list.addindex()
        
    
      
