#Generate a simple BST with insert() and inorder_traversal() methods.
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new node with the given key into the BST."""
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        """Helper method to insert a new node recursively."""
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def inorder_traversal(self):
        """Perform inorder traversal of the BST and return the keys in a list."""
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, node, result):
        """Helper method for inorder traversal recursively."""
        if node:
            self._inorder_rec(node.left, result)
            result.append(node.val)
            self._inorder_rec(node.right, result)
# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    print(bst.inorder_traversal())  # Output: [2, 3, 4, 5, 7]
    