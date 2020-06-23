# GOING OVER DOUBLY LINKED LIST


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

# focusing on delete for now

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            # self.next = a node, self.next.prev = that notes previous arrow, not the node
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # if list is currently empty, add node
        if self.head is None and self.tail is None:
            # set the head and tail to equal new node
            self.head = new_node
            self.tail = new_node
        else:
            # the list already has elements in it
            # make new nodes next value poine to current head
            new_node.next = self.head  # arrow to current head
            self.head.prev = new_node  # current head has new prev
            self.head = new_node  # set the head
        pass

    def remove_from_head(self):
        head_value = self.head.value
        self.delete(self.head)
        return head_value

    def add_to_tail(self, value):
        pass  # sam as head, but tail instead

    def remove_from_tail(self):
        if self.head is None:
            return
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value

    def move_to_front(self, node):
        if node is self.head:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_head(old_value)

    def move_to_end(self, node):
        if node is self.tail:
            return
        old_value = node.head_value
        self.delete(node)
        self.add_to_tail(old_value)

    def delete(self, node):
        # the list is empty -> do nothing:
        if self.head is None and self.tail is None:
            return
        # the list is only one node -> set head/tail accordingly
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # the node is the head node -> handle head pointer correctly
        elif self.head == node:
            # MOVE THE HEAD FIRST
            self.head = node.next  # MOVE HEAD FIRST
            node.delete()
        # the node is the tail node -> make sure tail is handled correctly
        elif self.tail == node:
            self.head = node.prev
            node.delete()
        # the node is just some node in the list ->  change 4 arrows
        else:
            node.delete()

    def get_max(self):
        pass
