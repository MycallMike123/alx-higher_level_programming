#!/usr/bin/python3

"""Class representing a node of a SLL."""


class Node:
    """Class representing a node of a SLL."""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): The data value for the node.
            next_node (Node): The next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data value of the node."""

        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the node with type validation."""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the linked list."""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list with type validation."""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class representing a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""

        self.head = None

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position in the list"""

        new_node = Node(value)

        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return

        temp = self.head
        while temp.next_node is not None and temp.next_node.data < value:
            temp = temp.next_node

        new_node.next_node = temp.next_node
        temp.next_node = new_node

    def display(self):
        """Print the entire list in stdout."""

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next_node

    def __str__(self):
        """String representation of the LL."""

        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(elements)
