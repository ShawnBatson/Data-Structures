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

    def remove_tail(self):
        if self.tail is None:
            return None
        data = self.tail.get_value()

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head

            while current.get_next != self.tail:
                current = current.get_next()
            self.tail = current
        return data

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
