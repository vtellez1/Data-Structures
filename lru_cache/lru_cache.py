from doubly_linked_list import DoublyLinkedList


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
        self.order = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order (Head)
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # Check if key-value exists
        if key in self.storage:
            # Moves pair to head so considederd most recent.
            node = self.storage[key]
            self.order.move_to_front(node)
            # return value associated with key
            return node.value[1]
        else:
            # Returns None if key-value doesn't exist
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache (Head). If the cache is already at max capacity
    before this entry is added, then the oldest entry (Tail) in the
    cache needs to be removed to make room. 
    
    Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # Check to see if key already exists
        # If exists,
        if key in self.storage:
            # overwrite old value with the key with newly-specified value
            node = self.storage[key]
            node.value = (key, value)
            # and move to front
            self.order.move_to_front(node)
            return node

        # If does not exist, check if cache is at max capacity.
        # If at max capacity, remove tail. Have to remove from storage and list
        if self.size == self.limit:
            self.storage.pop(self.order.remove_from_tail()[0])
            self.size -= 1
    # If not at max capacity
    # Add to cache as head
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        self.size += 1
