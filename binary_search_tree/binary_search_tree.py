import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.stack = Stack()
        self.queue = Queue()

    # Insert the given value into the tree
    def insert(self, value, node=None):
        # if the tree is empty, just make it the root
        if not self.value:
            node = self.value
            return 

        if not node:
            node = self
        
        # if attempting to insert duplicate, don't do that crap
        if node.value == value:
            node.right = BinarySearchTree(value)
            return value
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
    def contains(self, target, node=None):
        if not self.value:
            return False
        
        if not node:
            node = self

        # if the value is found, return true
        if node.value == target:
            return True
        # if root is greater than target, move left
        elif node.value > target:
            if node.left:
                return self.contains(target, node.left)
            else: 
                return False
        # if root is lesser than target, move right
        elif node.value < target:
            if node.right:
                return self.contains(target, node.right)
            else:
                return False
        


    # Return the maximum value found in the tree
    def get_max(self, node=None):
        if not self.value:
            return None

        if not node:      
            node = self

        # if you can move right, then move right silly boy
        if node.right:
            return self.get_max(node.right)
        else:
            return node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb, node=None):
        if not node:
            node = self
        
        cb(node.value)

        if node.left:
            self.for_each(cb, node.left)
        if node.right:
            self.for_each(cb, node.right)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        self.stack.push(node)

        if self.stack.size == 0:
            return 
        
        if self.stack.size > 0:
            print(self.stack.pop().value)
            if node.right:
                self.stack.push(node.right)
                self.in_order_print(self.stack.storage.head.value)
            if node.left:
                self.stack.push(node.left)
                self.in_order_print(self.stack.storage.head.value)
            else:
                return


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        self.queue.enqueue(node)

        if self.queue.size == 0:
            return 
        
        while self.queue.size > 0:
            print(self.queue.dequeue().value)
            if node.left:
                self.queue.enqueue(node.left)
            if node.right:
                self.queue.enqueue(node.right)
            if self.queue.size > 0:
                node = self.queue.storage.head.value
        return

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        self.stack.push(node)
        
        while self.stack.size > 0:
            print(self.stack.pop().value)
            if node.right:
                self.stack.push(node.right)
            if node.left:
                self.stack.push(node.left)
            if self.stack.size > 0:
                node = self.stack.storage.head.value      
        return 

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.dft_print(bst)