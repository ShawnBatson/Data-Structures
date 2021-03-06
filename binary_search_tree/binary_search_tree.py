from dll_queue.py import Queue
"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  # RECURSION NEEDED
        # compare to the new value we want to insert 8 root 3 insert
        if value < self.value:
            if self.left is not None:  # IF self.left is already taken by a node,
                self.left.insert(value)  # make that (left) node call insert.
            else:
                # set the left to the new node with the new value
                self.left = BSTNode(value)
        if value >= self.value:  # if new value is >= self.value
            if self.right is not None:  # IF self.right is taken by a node
                # make that (right) node call insert
                self.right.insert(value)
            else:
                # set the right child to the new node with new value.
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        found = False
        if self.value >= target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)
        # if current value >= target
        if self.value < target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
        found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree

    def get_max(self):
        # set the max value to a variable
        # move right from the first value, if there is no right, you are at the highest.
        max_value = self.value
        if self.right is None:
            return max_value
        else:
            max_value = self.right.get_max()
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call it on the original value
        # check to see if the current node has a left attribute that isn't None
        if self.left is not None:
            # then call this function on the left value if there is one
            self.left.for_each(fn)
        fn(self.value)
        # check to see if the current node has a right attribute that isn't None
        if self.right is not None:
            # Then call this function on the right value if there is one
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):  # node will be the first object used, root structure
        # if the left attribute is not none (node.left)
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        # add the first node to the queue
        # throw out a while loop:
        # While queue is not empty
        # remove the first node from the queue
        # print the removed node
        # add all children to the queue (left and right)
        # IF NODE HAS CHILDREN< ADD THEM TO THE QUEUE
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
