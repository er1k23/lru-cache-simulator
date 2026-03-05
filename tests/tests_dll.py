from lru_cache.doubly_linked_list import Node, DoublyLinkedList
def print_list(dll):
    current = dll.head.next
    result = []

    while current != dll.tail:
        result.append(f"{current.key}:{current.value}")
        current = current.next

    print(" <-> ".join(result))


def main():
    dll = DoublyLinkedList()

    # create nodes
    n1 = Node(1, 100)
    n2 = Node(2, 200)
    n3 = Node(3, 300)

    print("Add nodes to front")

    dll.add_front(n1)
    print_list(dll)

    dll.add_front(n2)
    print_list(dll)

    dll.add_front(n3)
    print_list(dll)

    print("\nMove node 1 to front")
    dll.move_to_front(n1)
    print_list(dll)

    print("\nRemove node 2")
    dll.remove(n2)
    print_list(dll)

    print("\nPop tail")
    tail_node = dll.pop_tail()

    print("Removed:", tail_node.key, tail_node.value)
    print_list(dll)


if __name__ == "__main__":
    main()