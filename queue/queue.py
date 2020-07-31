"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

import sys
sys.path.append('..')
from singly_linked_list.singly_linked_list import LinkedList  # pylint: disable=global-statement


class Queue:
    def __init__(self, storage=LinkedList()):
        self.size = 0
        self.storage = storage
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        return self.storage.shift()


# test_arr = [3, 4, 5, 6, 7]
test_linked_list = LinkedList()
linked_list_queue = Queue(test_linked_list)
linked_list_queue.enqueue(1)
linked_list_queue.enqueue(2)
linked_list_queue.enqueue(3)
linked_list_queue.dequeue()

print(len(test_linked_list))

# array_queue = Queue(test_arr)

# print(array_queue.storage)
linked_list_queue.storage.printLL()