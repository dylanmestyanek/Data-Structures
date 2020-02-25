import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dictionary = {}
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # To do this, change it's previous reference to the tail, and make that node the new tail
        # If the value doesn't exist, return None
        if key not in self.dictionary:
            return None
        # If the value exists, loop through the DLL and find that node and move it to the end
        elif key in self.dictionary:
            node = self.storage.head

            while node:
                if node.value[0] == key:
                    self.storage.move_to_end(node)
                    return self.dictionary[key]
                
                node = node.next

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # If key already exists, overwrite it
        if key in self.dictionary:
            self.dictionary[key] = value
        # If cache is at self.limit, then remove oldest key-value pair before adding new key-value pair
        elif self.size == self.limit:
            for i in self.dictionary:
                if self.dictionary[i] == self.storage.head.value[1]:
                    del self.dictionary[i]
                    break

            self.storage.remove_from_head()
            self.storage.add_to_tail((key, value))
            self.dictionary[key] = value
        # If the key doesn't exist, increase the size of the cache, and add a new key-value pair to the dictionary
        else:
            self.size += 1
            self.storage.add_to_tail((key, value))
            print(self.storage.tail.value)
            self.dictionary[key] = value

        return self.dictionary
