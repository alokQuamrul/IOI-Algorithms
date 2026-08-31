# ═══════════════════════════════════════════════════════
# Stack Using Two Queues — METHOD 2 (Pop-Heavy)
# Push: O(1)  |  Pop: O(n)  |  Top: O(n)
# ═══════════════════════════════════════════════════════

from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()   # primary queue
        self.q2 = deque()   # auxiliary queue

    def push(self, x):           # O(1) — no rearranging needed
        self.q1.append(x)

    def pop(self):                # O(n)
        if not self.q1:
            return

        # Step 1: Drain all but the last element into q2
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())

        # Step 2: The lone element remaining is the stack top — discard it
        self.q1.popleft()

        # Step 3: Swap — q2 is now the new q1
        self.q1, self.q2 = self.q2, self.q1

    def top(self):                # O(n)
        if not self.q1:
            return None

        # Step 1: Drain all but last element into q2
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())

        # Step 2: Read (but keep!) the last element
        top = self.q1[0]
        self.q2.append(self.q1.popleft())  # move it to q2 too

        # Step 3: Swap back — all elements restored to q1
        self.q1, self.q2 = self.q2, self.q1

        return top

    def size(self):               # O(1)
        return len(self.q1)

    def is_empty(self):          # O(1)
        return len(self.q1) == 0


# ── Driver Code ────────────────────────────────────────
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