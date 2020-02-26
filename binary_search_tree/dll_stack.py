import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # DLL is ideal for a stack due to it's ability to add and remove values from the head
        # The way a stack works, you can only remove items in the direction they were added
        # which is why DLL is ideal for tracking the order these values are stored
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
