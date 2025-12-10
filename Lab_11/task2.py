#Generate a Queue class with enqueue(), dequeue(), and is_empty() methods.
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue. 
        Raises IndexError if the queue is empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.items) == 0
# Example usage:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())  # Output: 1
    print(queue.is_empty())  # Output: False
    print(queue.dequeue())   # Output: 2
    print(queue.dequeue())   # Output: 3
    print(queue.is_empty())  # Output: True