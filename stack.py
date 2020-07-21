class stack:
    def __init__(self):
        self.items = []
    
    def push(self,value):
        return self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if (self.items == []):
            return True
        return False
    def peek(self):
        if  not self.is_empty():
            return self.items[-1]
    def display(self):
        print(self.items)

s = stack()
print("1: push \n 2:pop\n 3:is_empty\n 4:peek\n, 5: display\n ")

while (True):
    choice = int(input("Enter your choice:\n"))
    if choice  == 1:
        item = input("Enter a character:\n")
        s.push(item)
    elif (choice ==2):
        s.pop()
    elif( choice == 3):
        print( s.is_empty())
    elif(choice == 4):
        print(s.peek())
    elif (choice == 5):
        s.display()

# n = int(input("Enter the number of element you wish for your stack:\n"))

