from __future__ import annotations

from .hashmap import HashMap
from .doubly_linked_list import DoublyLinkedList, Node


class LRUCache:
    """
    LRU Cache:
      - HashMap: key -> Node (O(1) average lookup)
      - DoublyLinkedList: MRU near head, LRU near tail (O(1) move/evict)

    get(key):
      - return value if exists, else -1
      - if exists, move node to front (MRU)

    put(key, value):
      - insert/update
      - if at capacity and inserting new key -> evict LRU (tail.prev)
    """

    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("capacity must be >= 0")

        self.capacity = capacity
        self.map = HashMap()               # stores key -> Node
        self.list = DoublyLinkedList()     # stores Nodes in MRU->LRU order
        self.size = 0

    def get(self, key):
        node = self.map.get(key)
        if node is None:
            return -1

        # Mark as most recently used
        self.list.move_to_front(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        node = self.map.get(key)

        # If key exists: update value + move to MRU
        if node is not None:
            node.value = value
            self.list.move_to_front(node)
            return

        # If new key and cache is full: evict LRU
        if self.size == self.capacity:
            lru = self.list.pop_tail()
            # pop_tail() can return None only if list is empty (shouldn't happen here)
            if lru is not None:
                self.map.delete(lru.key)
                self.size -= 1

        # Insert new node at front
        new_node = Node(key, value)
        self.list.add_front(new_node)
        self.map.put(key, new_node)
        self.size += 1

    def items_mru_to_lru(self):
        """
        Helper for debugging / simulator:
        returns list of (key, value) from MRU to LRU.
        Requires your DLL to have to_list() like in earlier code.
        If you don't have to_list(), you can remove this method for now.
        """
        if hasattr(self.list, "to_list"):
            return self.list.to_list()
        # fallback: iterate manually if you have head/tail fields
        items = []
        cur = self.list.head.next
        while cur is not self.list.tail:
            items.append((cur.key, cur.value))
            cur = cur.next
        return items