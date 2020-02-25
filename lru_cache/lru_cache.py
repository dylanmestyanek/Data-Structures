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
        self.storage = DoublyLinkedList()
        self.dictionary = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # If the value doesn't exist, return None
        # If the value exists, moves it to the tail of the DLL as it was used
        # To do this, change it's previous reference to the tail, and make that node the new tail
        if key not in self.dictionary:
            return None
        elif key in self.dictionary:
            print(key)
            self.storage.move_to_front(self.dictionary[key])
            return self.dictionary[key]

        pass

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
        # Takes in key and value and needs to add it to self.dictionary
        # If cache is at self.limit, then remove oldest key-value pair before adding new key-value pair
        # If key already exists, overwrite it
        if key in self.dictionary:
            self.dictionary[key] = value
        elif self.size == self.limit:
            print(self.storage.tail)
            self.storage.remove_from_head()
            self.storage.add_to_tail(value)
            self.dictionary[key] = value
        else:
            self.size += 1
            self.storage.add_to_tail(value)
            self.dictionary[key] = value
        
        return self.dictionary

lru_cache = LRUCache(2)
print(lru_cache.set("one", 1))
print(lru_cache.set("two", 2))
print(lru_cache.set("three", 3))
print(lru_cache.set("one", 9))
