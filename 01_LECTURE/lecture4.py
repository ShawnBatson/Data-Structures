
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        found = False
        if self.value >= target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        if self.value < target:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found


## RECURSIVE STATE ##

    # Base case (not recursive)
    # Recursive case (repeats itself until you reach the base case)
        # START with a base case. This will have a clear definitive end.  If the code doesn't find a base case, it will repeat itself until it does.  This repetition is the recursion.

    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    def for_each(self, fn):
        if self.left:        # This is done IN ORDER.
            self.left.for_each(fn)
        fn(self.value)
        if self.right:
            self.right.for_each(fn)

# Lambda function (Not necessary, just lore/logic)
# javascript const print_node =(x) => { console.log }
# python: Lambda function is equivalent to the arrow function.
    # print_node = lambda x: print(x)


# TREE TRAVERSALS!!
    # Visit each node once, and probably do something
# DEPTH FIRST TRAVERSAL:
    # prioritize going deep.  The FOR EACH ABOVE IS ALREADY DEPTH FIRST
# BREADTH FIRST TRAVERSAL:
    # print initial, and then both it's children first.

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


def dft_print(self, node):
    # use iterative
    # Same as above, but use stack.
    # CREATE A STACK FOR NODES
    # add first node to stack.
    # while the stack is not empty
    # get the current node from top of stack
    # print that node
    # ADD ALL CHILDREN TO STACK,
    # keep in mind order that you add children will matter.

    pass
