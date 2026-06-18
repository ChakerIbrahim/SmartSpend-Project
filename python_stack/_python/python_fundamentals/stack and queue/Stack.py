from Node import Node
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        return self
    
    def pop(self):
        if self.head is None:
            print("Stack is Empty")
            return None
    
        remove = self.head
        self.head = self.head.next
        return remove.value
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.value
    
    def empty(self):
        return self.head is None
    
    def display(self):
        current = self.head
        while current:
            print(current.value,end= "=>")
            current = current.next
        print("Null")