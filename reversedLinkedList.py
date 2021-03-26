class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        self.item = item
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def reverse(self):
        """
        program to reversed a linkedlist in python
        1-->2 --> 3 --> 5 --> Null
        prev: refer to previous node
        temp: the current node
        head: the head point
        """
        prev = None
        temp = self.head
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
            self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


link = linkedList()
link.append(1)
link.append(2)
link.append(9)
link.append(3)
link.append(5)
print("The original linked list is: ")
link.display()
print("The reversed linkedlist is: ")
link.reverse()
link.display()
