from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

#Queues - FIFO


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # A: In real world cases, Linked Lists can be used to create queues and stacks
        self.storage = DoublyLinkedList()

# enqueue should add an item to the back of the queue.
    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)


# dequeue should remove and return an item (the item we're removing) from the front of the queue.

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            removed_head = self.storage.head.value
            self.storage.remove_from_head()
            return removed_head

# len returns the number of items in the queue.
    def len(self):
        return self.size
