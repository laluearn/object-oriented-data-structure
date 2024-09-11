class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            now = self.root
            while now:
                if data < now.data:
                    if not now.left:
                        now.left = Node(data)
                        break
                    now = now.left
                else:
                    if not now.right:
                        now.right = Node(data)
                        break
                    now = now.right
        else:
            self.root = Node(data)
        return self.root

    def preOrder(self, root):
        if not root:
            return
        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)

    def postOrder(self, root):
        if not root:
            return
        self.postOrder(root.left)  
        self.postOrder(root.right)
        print(root.data, end=" ")

    def breadth(self, root):
        if not root:
            return
        queue = [self.root]
        values = []
        val = ""
        while len(queue):
            now = queue.pop(0)
            values.append(now.data)
            if now.left:
                queue.append(now.left)
            if now.right:
                queue.append(now.right)
        for ele in values:
            val += str(ele) + " "
        print(val)

inp = [int(num) for num in input("Enter Input : ").split()]

T = BST()
for i in inp:
    root = T.insert(i)
print(f"Preorder : ", end="")
T.preOrder(T.root)
print(f"\nInorder : ", end="")
T.inOrder(T.root)
print(f"\nPostorder : ", end="")
T.postOrder(T.root)
print(f"\nBreadth : ", end="")
T.breadth(T.root)