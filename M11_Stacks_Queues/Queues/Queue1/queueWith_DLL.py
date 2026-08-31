# ── NODE CLASS
class Node:
    def __init__(self, data):
        self.data = data    # The actual value we want to store
        self.next = None    # Looks FORWARD — towards the rear of the queue
        self.prev = None    # Looks BACKWARD — towards the front of the queue (NEW!)


# ── QUEUE CLASS (using the doubly linked list)
class Queue:
    """
    A Queue (FIFO) built on top of a doubly linked list.
    We still only ever touch the FRONT and REAR ends —
    we never need to walk through the middle of the list.
    """

    def __init__(self):
        self.front = None   # The first node — this is where we DEQUEUE from
        self.rear  = None   # The last node  — this is where we ENQUEUE to
        self._size = 0      # Keeps count so size() is instant (O(1))

    # ── IS EMPTY 
    def is_empty(self):
        """
        A queue is empty when there is no front node at all.
        Returns True / False.
        """
        return self.front is None

    # ── SIZE ────────────────────────────────────────────────────
    def size(self):
        """Returns how many elements are currently in the queue."""
        return self._size

    # ── ENQUEUE  (add to the REAR) ──────────────────────────────
    def enqueue(self, data):
        """
        Adds a new element to the back (rear) of the queue.
        Time complexity: O(1) — we never search, we only touch
        the rear pointer directly.
        """
        # STEP 1: Build the new node. It starts completely disconnected —
        #         both prev and next are None until we link it below.
        new_node = Node(data)

        if self.is_empty():
            # STEP 2a: Special case — queue was totally empty.
            #          This one node becomes BOTH the front and the rear.
            self.front = new_node
            self.rear  = new_node
        else:
            # STEP 2b: Queue already has elements — attach the new node
            #          AFTER the current rear node.

            # (i)  The new node looks BACKWARD at the current rear.
            #      This is the "doubly" part that's different from a
            #      singly linked list!
            new_node.prev = self.rear

            # (ii) The current rear now looks FORWARD at the new node.
            self.rear.next = new_node

            # (iii) Finally, move the rear pointer so it now points
            #       to our brand-new node — it's the new "last" element.
            self.rear = new_node

        self._size += 1
        print(f"Enqueued: {data}")

    # ── DEQUEUE  (remove from the FRONT) ────────────────────────
    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.
        Time complexity: O(1).
        """
        if self.is_empty():
            # Nothing to remove — this is called "underflow"
            print("Queue Underflow! Cannot dequeue from empty queue.")
            return None

        # STEP 1: Remember the data before we lose access to the node.
        removed_data = self.front.data

        # STEP 2: Move the front pointer one step forward.
        #         The 2nd element becomes the new front.
        self.front = self.front.next

        if self.front is None:
            # STEP 3a: The queue is now completely empty —
            #          there's no new front, so there's no rear either.
            self.rear = None
        else:
            # STEP 3b: *** THIS LINE IS NEW vs. singly linked list! ***
            #          The new front node should no longer look backward
            #          at the node we just removed. We clear that link so
            #          nothing points to the removed node anymore.
            self.front.prev = None

        self._size -= 1
        print(f"Dequeued: {removed_data}")
        return removed_data

    # ── PEEK  (look at front without removing) ──────────────────
    def peek(self):
        """Returns the front element's data WITHOUT removing it."""
        if self.is_empty():
            print("Queue is empty — nothing to peek at.")
            return None
        return self.front.data

    # ── DISPLAY FORWARD  (front → rear) ─────────────────────────
    def display_forward(self):
        """Prints every element starting from front, moving to rear."""
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front          # Start walking from the front
        elements = []
        while current:                   # Keep going until we fall off the end (None)
            elements.append(str(current.data))
            current = current.next       # Step forward using the 'next' pointer
        print("Front → Rear:", " ⇄ ".join(elements))

    # ── DISPLAY BACKWARD  (rear → front)  *** ONLY POSSIBLE
    #     BECAUSE THIS IS A DOUBLY LINKED LIST! *** ─────────────
    def display_backward(self):
        """
        Prints every element starting from the REAR, moving
        backward to the FRONT. A singly linked list CANNOT do
        this easily — it would need to restart from the front
        every single time. We can do it directly because every
        node remembers what comes before it.
        """
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.rear            # Start walking from the rear this time
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev       # Step BACKWARD using the 'prev' pointer
        print("Rear → Front:", " ⇄ ".join(elements))


# ── DRIVER CODE — let's test it! ─────────────────────────────────
if __name__ == "__main__":
    q = Queue()

    print("=== Building a matchmaking queue ===")
    q.enqueue("Player_One")
    q.enqueue("Player_Two")
    q.enqueue("Player_Three")

    q.display_forward()    # Player_One ⇄ Player_Two ⇄ Player_Three
    q.display_backward()   # Player_Three ⇄ Player_Two ⇄ Player_One

    print(f"\nQueue size : {q.size()}")
    print(f"Front item : {q.peek()}")

    print("\n--- Matching players one by one ---")
    q.dequeue()
    q.display_forward()

    q.dequeue()
    q.dequeue()
    q.dequeue()  # This will print the underflow message