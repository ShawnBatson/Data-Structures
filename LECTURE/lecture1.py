# EFFICIENTly RUN TIME COMPLEXITH

# it's not about how fast the computer runs something, the time is not important, the important part is: how does the algorithm keep performing the more information we put into it.  If it goes slower and slower, then its a bad algorithm

# Read the internals of the functions to understand the time complexity marker of the parent function.
import math
from math import sqrt

# to analyze big O,
# 1. does the number of steps increase if input increases
#     (n) below will not add steps because the only step is just a number.  This is called CONSTANT RUNTIME


def mult_2(n):
    return n * 2

# 2. go line by line, figure out what each big-O is, and add.


def foo(n):  # O(n) or Linear time
    for i in range(0, n):  # This will run N times. O(n)
        # the total runtime of the code in the loop is O(1)
        print(i)  # O(1)
        print(i)  # O(1)

# 3.1 if loop: look at the code inside, and repeast step 2
# 3.2 calculate how many times, the loop will run
# 3.3 result of 3.1  multiplied by result of 3.2

# QUADRATIC TIME OR POLYNOMIAL TIME


def bar(n):  # O(1) + O(n^2) + O(1) ==> O(n^2) = worst case
    s = 0  # O(1)
    # O(n) * O(n) = O(n^2)
    for i in range(0, n):  # O(n)
        for j in range(0, n):  # O(n) this loop runs linear
            s += i + j  # 0(1)

    return s  # O(1)

# O(n) * O(sqrt(n)) == O(n * sqrt(n))


def baz(n):
    s = 0

    for i in range(n):
        for j in range(int(sqrt(n))):  # O(sqrt(n)) or as this: O(n^0.5)
            s += i * j  # O(1)

# n = 8, number of steps = 3 times
# n = 16, number of steps = 4 times
# n = 32, number of steps = 5 steps
# THIS IS CALLED SUBLINEAR, SO LOGARITHMIC
# THIS IS A LOGARITHMIC FUNCTION
# O(log(n))


def divider(n):  # O(log(n))
    while n >= 1:
        print(n)  # O(1)
        n = n // 2  # O(1)
        # if size divides, then it's logarithmic

####################################################
####################################################
####################################################

# DATA STRUCTURES

    # Want some way to access data
        # arr[3]  =  O(1)
        # data.struct.read()

    # O(n) insertion:
        # array.append
        # dict("new key") = value
    # O(n) delete
    # search

    # LINKED LIST
        # A bunch of values literally linked to each other
        # accessing data is not the same.
        # NOT stored in an actual line, but stored with pointers to the next spot, so removing/adding does not take that much time or effort

# Making a linked list


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

# this has to know where the HEAD(start) and TAIL(end) of the linked list is


class LinkedList:
    def __init__(self):
        self.head = None  # stores a node that corresponds to our first node in the list
        self.tail = None  # stores a node that is the end of said list

    def add_to_head(self, value):
        # create a new node to add
        new_node = Node(value)
        # Check if list is empty
        # if head + tail = None, it is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a new node to add
        new_node = Node(value)
        # Check if list is empty
        # if head + tail = None, it is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail to new node
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        # move the head to the new correct location
        # once moved, the old head will be garbage collected
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list has only one element, set head and tail to none
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise, we have more elements in list,
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node until you see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            current_node = current_node.next_node
        return False


linked_list = LinkedList()

linked_list.add_to_head(0)
linked_list.add_to_tail(1)
print(f"does our LL contain 0? {linked_list.contains(0)}")
print(f"does our LL contain 0? {linked_list.contains(1)}")

linked_list.add_to_head(2)
print(f"the start of the list is {linked_list.head.value}")
linked_list.add_to_head(5)
print(f"the start of the list is {linked_list.head.value}")
