class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        # sentinel nodes
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def move_to_front(self, node):
        self.remove(node)
        self.add_front(node)

    def pop_tail(self):
        node = self.tail.prev
        if node == self.head:
            return None

        self.remove(node)
        return node

    def get_lru(self):
        node = self.tail.prev
        if node == self.head:
            return None
        return node