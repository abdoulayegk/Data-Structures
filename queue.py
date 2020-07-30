# write a programme to implement queue data structure with its various operations
#A Queue is a FIFO (First In First Out) data structure where the element that is added first will be deleted first.
#The basic queue operations are enqueue (insertion) and dequeue (deletion). Enqueue is done at the front of the queue and dequeue is done at the end of the queue.

class Queue:
    def __init__(self):
        self. listQ = [] # here we are going to store all the elements of the queue
    def queue(self,value):
        return self.listQ.insert(0,value)

    def dequeue(self):
        return self.listQ.pop()
    def display(self):
        print(self.listQ)
    def length(self):
        print('The length of the queue is:', len(self.listQ))
q = Queue()
while True:
    print('\n 1-queue \n 2-dequeue\n 3-display\n 4-Length\n,5- Exit(0)\n')
    choice = int(input("Enter your choice:\n"))
    if choice == 1:
        q.queue(input('Enter an alphabet: '))
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
       q.display()
    elif choice == 4:
        q.length()
    else:
        break
