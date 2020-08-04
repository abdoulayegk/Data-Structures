class Node:
    def __init__(self,data):
        self.data = data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
    def delete_first(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            self.head = self.head.next

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data,'-->', end = '')
            temp = temp.next

linked =  LinkedList()
linked.insert('A')
linked.insert('B')
linked.delete_first()
linked.insert('C')
linked.insert('D')

linked.display()

