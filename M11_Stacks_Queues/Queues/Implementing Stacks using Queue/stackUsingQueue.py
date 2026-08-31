# ═══════════════════════════════════════════════════════
# Stack Using Two Queues — METHOD 1 (Push-Heavy)
# Push: O(n)  |  Pop: O(1)  |  Top: O(1)
# ═══════════════════════════════════════════════════════

from collections import deque as dq

class Stack:
    def __init__(self):
        # q1 = main queue (always holds elements in FIFO order)
        # q2 = temporary auxiliary queue
        self.q1 = dq()
        self.q2 = dq()

    def push(self, x):           # O(n)
        # Step 1: Enqueue new element into empty q2
        self.q2.append(x)

        # Step 2: Move ALL of q1 into q2
        #   ➜ new element is now at the FRONT of q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Step 3: Swap names — q1 now has correct LIFO order
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):                # O(1)
        # Front of q1 is always the stack top — just dequeue it
        if self.q1:
            self.q1.popleft()

    def top(self):                # O(1)
        # Peek at front without removing
        if self.q1:
            return self.q1[0]
        return None

    def size(self):               # O(n)
        return len(self.q1)

    def is_empty(self):          # O(1)
        return self.q1 == None


if __name__ == '__main__':
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)

    print("Current size:", s.size())    # Output: 3
    print("Top:", s.top())              # Output: 3

    s.pop()
    print("Top after pop:", s.top())    # Output: 2

    s.pop()
    print("Top after pop:", s.top())    # Output: 1

    print("Current size:", s.size())    # Output: 1
    print("Is empty?", s.is_empty())   # Output: False
    