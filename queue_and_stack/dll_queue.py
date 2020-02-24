import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import ListNode, DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # DLL is a good choice to store our elements because it is an efficient way to manipulate the queue
        # DLL allows us to add items to the tail (enqueue) and remove items from the head (dequeue)
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size