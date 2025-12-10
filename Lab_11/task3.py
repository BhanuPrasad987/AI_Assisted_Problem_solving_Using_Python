#Create a singly linked list with insert_at_end(), insert_at_beginning(), and display() methods
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_beginning(self, data):
        """Insert a new node with the given data at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        """Display the linked list."""
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))
# Example usage:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_beginning(0)
    linked_list.display()  # Output: 0 -> 1 -> 2