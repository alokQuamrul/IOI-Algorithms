    # ── NODE CLASS 
class Node:
    def __init__(self, data):
        self.data = data   # Value stored in this node
        self.next = None   # Pointer to next node (None = end of list)


# ── QUEUE CLASS 
class Queue:

    def __init__(self):
        self.front = None  # Points to the FRONT node (dequeue here)
        self.rear  = None  # Points to the REAR  node (enqueue here)
        self._size = 0     # Track size for O(1) size queries #_ means its protected

    # ── IS EMPTY
    def is_empty(self):
        """Return True if the queue has no elements."""
        return self.front is None

    # ── SIZE ────────────────────────────────────────────────────
    def size(self):
        """Return the number of elements currently in the queue."""
        return self._size

    # ── ENQUEUE ─────────────────────────────────────────────────
    def enqueue(self, data):
        """Insert an element at the REAR of the queue. O(1)."""
        new_node = Node(data)          # 1. Create a new node

        if self.is_empty():
            # 2a. Queue was empty — front & rear both point to new node
            self.front = new_node
            self.rear  = new_node
        else:
            # 2b. Link current rear to new node, then advance rear
            self.rear.next = new_node
            self.rear      = new_node

        self._size += 1                 # 3. Increment size counter
        print(f"Enqueued: {data}")

    # ── DEQUEUE ─────────────────────────────────────────────────
    def dequeue(self):
        """Remove and return the FRONT element. O(1)."""
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue from empty queue.")
            return None

        removed_data = self.front.data  # 1. Save front's data
        self.front = self.front.next   # 2. Move front pointer forward

        if self.front is None:
            # 3. Queue is now empty — also reset rear to None
            self.rear = None

        self._size -= 1                 # 4. Decrement size counter
        print(f"Dequeued: {removed_data}")
        return removed_data

    # ── PEEK ────────────────────────────────────────────────────
    def peek(self):
        """Return the FRONT element without removing it. O(1)."""
        if self.is_empty():
            print("Queue is empty — nothing to peek at.")
            return None
        return self.front.data

    # ── DISPLAY ─────────────────────────────────────────────────
    def display(self):
        """Print all elements from front to rear. O(n)"""
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Queue [FRONT → REAR]:", " → ".join(elements))


# ── DRIVER CODE ─────────────────────────────────────────────────
if __name__ == "__main__":
    q = Queue()
    q.display()

    # Enqueue players into a respawn queue
    q.enqueue("Player_Alpha")
    q.enqueue("Player_Beta")
    q.enqueue("Player_Gamma")
    q.enqueue("Player_Delta")

    q.display()
    print(f"Queue size : {q.size()}")
    print(f"Front item : {q.peek()}")

    print("\n--- Processing Respawn Queue ---")
    q.dequeue()
    q.dequeue()
    q.display()

    print(f"\nIs queue empty? {q.is_empty()}")
    q.dequeue()
    q.dequeue()
    q.dequeue()  # This will trigger underflow message