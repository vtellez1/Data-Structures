from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

# Stacks - LIFO (Last one in, first one out like plates stacked up)


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # A: In real world cases, Linked Lists can be used to create queues and stacks
        self.storage = DoublyLinkedList()

# Add item to the end
    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

# Remove item from the end
    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            removed_item = self.storage.tail.value
            self.storage.remove_from_tail()
            return removed_item

    def len(self):
        return self.size
