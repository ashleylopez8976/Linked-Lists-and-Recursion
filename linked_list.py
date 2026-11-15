class Node:
    """Store data and a reference to the next node."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list with recursive operations."""

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """Recursively add each node's data."""

        def sum_nodes(node):
            # Base case: no more nodes to add.
            if node is None:
                return 0

            # Recursive case: add this value to the remaining sum.
            return node.data + sum_nodes(node.next)

        return sum_nodes(self.head)

    def recursive_reverse(self):
        """Recursively reverse links without creating new nodes."""

        def reverse_nodes(prev, current):
            # Base case: the previous node becomes the new head.
            if current is None:
                return prev

            next_node = current.next
            current.next = prev

            # Recursive case: continue with the next original node.
            return reverse_nodes(current, next_node)

        self.head = reverse_nodes(None, self.head)

    def recursive_search(self, target):
        """Recursively check nodes for the target value."""

        def search_nodes(node):
            # Base case: reached the end without finding the target.
            if node is None:
                return False

            if node.data == target:
                return True

            # Recursive case: search the rest of the list.
            return search_nodes(node.next)

        return search_nodes(self.head)

    def display(self):
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.data))
            current = current.next

        values.append("None")
        print(" -> ".join(values))