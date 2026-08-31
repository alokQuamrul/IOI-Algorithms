#Stack Implementation Using Linked List (Python) 
class Node:
    def __init__(self, data):
        self.data = data   # The value stored in this node
        self.next = None   # Pointer to the node below it


class StackLL:
    def __init__(self):
        self.top  = None   # Points to the top node
        self._size = 0

    # Push: create a new node, point it to current top, update top
    def push(self, value):
        new_node      = Node(value)
        new_node.next = self.top    # New node points to old top
        self.top      = new_node    # Update top to new node
        self._size   += 1
        print(f"Pushed: {value}")

    # Pop: save top's value, move top to next node
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
            return None
        popped_val    = self.top.data
        self.top      = self.top.next  # Move top pointer down
        self._size   -= 1
        return popped_val

    # Peek: just read top's data
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Stack (top → bottom):", " → ".join(elements))


if __name__ == "__main__":
    s = StackLL()

    s.push("SWORD")
    s.push("SHIELD")
    s.push("POTION")
    s.push("MAP")

    s.display()                         
    print("Top item:", s.peek())         
    print("Used item:", s.pop())            
    print("Inventory size:", s.size()) 