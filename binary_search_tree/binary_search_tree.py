import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value, node=None):
        # if the tree is empty, just make it the root
        if not self.value:
            node = self.value
            return 
        if not node:
            node = self
        
        # if its less than root, move down left subtree,
        if node.value > value:
            if node.left:
                self.insert(value, node.left)
            else:
                node.left = BinarySearchTree(value)
                return value
        # if its more than root, move down right subtree
        elif node.value < value:
            if node.right:
                self.insert(value, node.right)
            else:
                node.right = BinarySearchTree(value)
                return value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BinarySearchTree(4)
print(bst.value)
# print(bst.left)
bst.insert(2)
bst.insert(6)
print(bst.left.value)
print(bst.right.value)
bst.insert(3)
print(bst.left.right.value)
bst.insert(1)
print(bst.left.left.value)