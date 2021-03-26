class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self,data):
        New_node = Node(data)
        if self.head is None:
            self.head = New_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = New_node
    def insert_first(self,data):
        New_node = Node(data)

        New_node.next = self.head
        self.head = New_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,'-->', end = ' ',)
            temp = temp.next


l = LinkedList()
n = int(input("Enter the number of element for your linked list: "))
for i in range(n):
    l.insert_end(input("Enter an alphabet: "))
l.display()

print("\n\n")

l.insert_first(input("Enter the alphabet to insert at the first position: "))
l.display()
