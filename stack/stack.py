from linked_list import LinkedList
from linked_list import Node

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""

# BELOW IS PART #1

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self._data = []

#     def __len__(self):
#         return len(self._data)

#     def is_empty(self):
#         return len(self._data) == 0

#     def push(self, value):
#         self._data.append(value)

#     def pop(self):
#         if self.is_empty():
#             return None
#         else:
#             return self._data.pop(-1)

###################BELOW IS PART 2########################


class Stack:
    def __init__(self):
        self.head = None

    def __len__(self):
        pointer = self.head
        count = 0

        while(pointer):
            count += 1
            pointer = pointer.next_node
        return count

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next_node = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            head_node = self.head
            self.head = head_node.next_node
            head_node.next_node = None
            return head_node.value

############### PART 3 BELOW ###################

# ANSWER:  An array can be accessed via an index pointer.  A linked list, each separate element points to the next element, so when removing or adding, you have to change where the pointers are pointing.
