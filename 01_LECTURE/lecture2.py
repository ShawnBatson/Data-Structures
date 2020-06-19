from linked
# Data structures will have common actions/operations
# insert (front or back) values
# read values
# delete values
# search

# LETS EXAMINE ADDING TO HEAD
# If the list is empty, Head and Tail are both None.
# If list has one element in it, head and tail equal the element
# If list has several elements in it, 1 or more, then, to add to it, we must be careful not to touch the tail.
# we're inserting a 2, if the new value is going to be the head of the linked list, we must move the head to that value, we then must link the new value to the tail.
# === new_node.next_node = self.head ==== we are setting up the link before MOVING the head. otherwise, we lose the link.  Then we set the new head value with === self.head = new_node ====
#  ADD THE NODE, MAKE THE LINK, MOVE THE HEAD
#############################################
# ADD THE NOODE, MAKE THE LINK, MOVE THE TAIL (for tail insertion)

# THIS IS MEMORIZABLE. MEMORIZE THIS
#   def __str__(self):

# output = ''  # MAKE SURE A CONTAINER IS MADE
# current_node = self.head  # create tracker

# while current_node is not None:  # loop until it's none

# update the tracker node to next node
#output += f'{current_node.value} => '

# current_node = current_node.next_node  # move the head.


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
# MEMORIZE THIS HERE V V V V V V V V V V V

    def __str__(self):
        output = ''  # MAKE SURE A CONTAINER IS MADE
        current_node = self.head  # create tracker node variable

        while current_node is not None:  # loop until it's none

            # update the tracker node to next node
            output += f'{current_node.value} => '

            current_node = current_node.next_node  # move the head.

    def add_to_head(self, value):

        new_node = Node(value)  # create new node

        if self.head is None and self.tail is None:   # if list is empty,
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head  # new_node needs to point to current head
            self.head = new_node  # move pointer to the new node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None

        current_max = self.head.get_value()

        current = self.head.get_next()

        while current is not None:
            if current.get_value() > current_max:
                current_max = current.get_value()

            current = current.get_next()
        return current_max


class StackArray:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.insert(0, value)

    def pop(self, value):
        if len(self.storage) == 0:
            return None
        self.size -= 1
        node = self.storage.pop(0)
        return node


class StackLL:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        pass

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size - + 1
        node = self.storage.remove_head()
        return node


class QueueLL:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            value = self.storage.remove_head()
            return value
