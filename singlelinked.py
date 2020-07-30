class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head  = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_first(self,data):
        new_node = Node(data)
 
        new_node.next = self.head
        self.head = new_node


    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

l = linkedList()
l.insert_last("A")
l.insert_last("B")
l.insert_first("X")
l.display()
