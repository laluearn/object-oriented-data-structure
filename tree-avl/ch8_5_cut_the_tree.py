class BST:
    class BSTNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, root=None) -> None:
        self.root = root

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def search_subtree(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search_subtree(root.left, key)
        else:
            return self.search_subtree(root.right, key)

    def insert(self, root, key):
        if root is None:
            return self.BSTNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def delete_subtree(self, root, key):
        deleted = self.search_subtree(root, key)
        parent = self._find_parent(root, deleted)
        if parent is None:
            return None
        if parent.left == deleted:
            parent.left = None
        else:
            parent.right = None
        return root

    def _find_parent(self, root, node):
        if root is None or root == node:
            return None
        if (root.left == node) or (root.right == node):
            return root
        if node.val < root.val:
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.printTree90(root.left, indent + 1)

class AVLTree:
    class AVLNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right
            self.height = 1

    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, root, key):
        if not root:
            return self.AVLNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        # update heights
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)
        if balance > 1 and key < root.left.val:
            root = self.right_rotate(root)
        elif balance < -1 and key >= root.right.val:
            root = self.left_rotate(root)
        elif balance > 1 and key >= root.left.val:
            root.left = self.left_rotate(root.left)
            root = self.right_rotate(root)
        elif balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            root = self.left_rotate(root)
        return root

    def left_rotate(self, z):
        new_root = z.right
        z.right = new_root.left
        new_root.left = z
        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def right_rotate(self, z):
        new_root = z.left
        z.left = new_root.right
        new_root.right = z
        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right)

    def bst_to_avl(self, bst_root):
        # Convert BST to sorted list via in-order traversal
        sorted_values = self.inorder_traversal(bst_root)
        # Insert elements into the AVL tree
        for val in sorted_values:
            self.root = self.insert(self.root, val)

    def inorder_traversal(self, root):
        # Helper function to perform in-order traversal and return a sorted list
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.val]
            + self.inorder_traversal(root.right)
        )

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.printTree90(root.left, indent + 1)


inp1, inp2 = input("Enter the val of tree and node to cut: ").split("/")
bst = BST()
for i in inp1.split():
    bst.root = bst.insert(bst.root, int(i))
print("Before cut:")
bst.printTree90(bst.root)
avl1, avl2 = AVLTree(), AVLTree()

# Convert the found subtree into an AVL tree
print("Cutted Tree:")
subtree_root = bst.search_subtree(bst.root, int(inp2))
avl1.bst_to_avl(subtree_root)
avl1.printTree90(avl1.root)

# Convert the remaining BST (after deletion) into an AVL tree
print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(inp2))
avl2.bst_to_avl(bst.root)
avl2.printTree90(avl2.root)
