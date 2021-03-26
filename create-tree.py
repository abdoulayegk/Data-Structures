class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def create(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.create(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.create(data)
        else:
            self.data = data

    # for inorder traversal of the tree to display the elements

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print('\n[{}]\n'.format(self.data), end=' '),
        if self.right:
            self.right.inOrder()


tree = Tree(8)
tree.create(7)
tree.create(6)
tree.create(4)
tree.create(2)
tree.create(5)
tree.inOrder()
