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

    def insert(self, root, data):
        if not root:
            return AVLNode(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        balance = self.getBalance(root)
        if balance < -1 or balance > 1:
            # left left case
            if balance > 1 and data < root.left.data:
                root = self.rotateRight(root)
                print("Right Right Rotation")
            # right right case
            elif balance < -1 and data >= root.right.data:
                root = self.rotateLeft(root)
                print("Left Left Rotation")
            # left right case
            elif balance > 1 and data >= root.left.data:
                root.left = self.rotateLeft(root.left)
                root = self.rotateRight(root)
                print("Left Right Rotation")
            # right left case 
            elif balance < -1 and data < root.right.data:
                root.right = self.rotateRight(root.right)
                root = self.rotateLeft(root)
                print("Right Left Rotation")
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

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

myTree = AVLTree() 
root = None
print(" *** AVL Tree Insert Element ***")
data = [int(i) for i in input("Enter Input : ").split()]
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("====================")