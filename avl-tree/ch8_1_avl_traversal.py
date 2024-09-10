class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class AVLTree:
    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        if not root:
            return AVLNode(data)
        if data < root.data:
            root.left = self._add(root.left, data)
        else:
            root.right = self._add(root.right, data)


        balance = self.getBalance(root)
        # left left case
        if balance > 1 and data < root.left.data:
            root = self.rotateRight(root)
        # right right case
        elif balance < -1 and data >= root.right.data:
            root = self.rotateLeft(root)
        # left right case
        elif balance > 1 and data >= root.left.data:
            root.left = self.rotateLeft(root.left)
            root = self.rotateRight(root)
        # right left case 
        elif balance < -1 and data < root.right.data:
            root.right = self.rotateRight(root.right)
            root = self.rotateLeft(root)
        return root

    def rotateRight(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root

    def rotateLeft(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root

    def getHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right)

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)
    
    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end = " ")

avl1 = AVLTree()
# inp = [int(num) for num in input("Enter Input : ").split(",")]
inp = input("Enter Input : ").split(",")
for i in inp:
    if i[:2] == "AD":
        avl1.add(int(i[3:]))
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        if avl1.root:
            print("AVLTree post-order :", end = " ")
            avl1.postOrder(avl1.root)
        else:
            print("AVLTree post-order : ")
        print()