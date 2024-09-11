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
            current = self.root
            while current:
                if data < current.data:
                    if not current.left:
                        current.left = Node(data)
                        break
                    current = current.left    
                else:
                    if not current.right:
                        current.right = Node(data)
                        break
                    current = current.right
        else:
            self.root = Node(data)
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

inp = input("Enter Input : ").split("|")
nums = [int(num) for num in inp[0].split()]

T = BST()
for i in nums:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")

below = []

for items in nums:
    if items < int(inp[1]):
        below.append(items)

if below == []:
    print(f"Below {inp[1]} : Not have")
else:
    for i in range(len(below)):
        for j in range(i + 1, len(below)):
            if below[i] >= below[j]:
                below[i], below[j] = below[j], below[i]

    print(f"Below {inp[1]} : ", end = "")

    for index in range(len(below)):
        print(below[index], end = " ")