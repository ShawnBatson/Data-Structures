from linked_list import LinkedList
from linked_list import Node


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
##############BELOW IS PART #1 #####################################

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self._data = []

#     def __len__(self):
#         return len(self._data)

#     def is_empty(self):
#         return len(self._data) == 0

#     def enqueue(self, value):
#         self._data.append(value)

#     def dequeue(self):
#         if self.is_empty():
#             return None
#         else:
#             return self._data.pop(0)   # this is the first in first out part.

##################BELOW IS PART #2#################################


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._data = []
        self.count = 0

    def __len__(self):
        pointer = self.head
        counter = 0

        while(pointer):
            counter += 1
            pointer = pointer.next_node
        return counter

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)

        if self.tail is not None:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return None
        if self.head is not None:
            head_value = self.head.value
            self.head = self.head.next_node
            return head_value


############### PART 3 BELOW ###################

# ANSWER:  An array can be accessed via an index pointer.  A linked list, each separate element points to the next element, so when removing or adding, you have to change where the pointers are pointing.
