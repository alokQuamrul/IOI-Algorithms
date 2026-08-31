class DoubleStackOptimized:
    def __init__(self, capacity):  #capacity == size of the combined array
        self.capacity = capacity   # total size of the single array
        self.arr = [None] * capacity # one array holding both stacks
        self.top1 = -1             # stack1 starts empty from left
        self.top2 = capacity       # stack2 starts empty from right

    # ----- Stack 1 (left side) -----
    def push1(self, item):
        if self.top1 + 1 == self.top2:
            raise OverflowError("Double stack is full. You cant push anymore")
        self.top1 += 1
        self.arr[self.top1] = item

    def pop1(self):
        if self.top1 == -1:
            raise IndexError("Stack1 is empty")
        item = self.arr[self.top1]
        self.arr[self.top1] = None # optional: clear reference
        self.top1 -= 1
        return item

    def peek1(self):
        if self.top1 == -1:
            raise IndexError("Stack1 is empty")
        return self.arr[self.top1]

    def is_empty1(self):
        return self.top1 == -1 #TC:O(1) but if I used len() the TC:O(n)
    

    # ----- Stack 2 (right side) -----
    def push2(self, item):
        if self.top1 + 1 == self.top2:
            raise OverflowError("Double stack is full")
        self.top2 -= 1
        self.arr[self.top2] = item

    def pop2(self):
        if self.top2 == self.capacity:
            raise IndexError("Stack2 is empty")
        item = self.arr[self.top2]
        self.arr[self.top2] = None
        self.top2 += 1
        return item

    def peek2(self):
        if self.top2 == self.capacity:
            return None
        return self.arr[self.top2]

    def is_empty2(self):
        return self.top2 == self.capacity


    def display(self):
        for i in range(self.capacity):
            print(f"{self.arr[i] if i < self.capacity else ""}",end="=>")
        print()
    

double_stack = DoubleStackOptimized(6)
double_stack.display()
double_stack.push1("A")
double_stack.push1("B")
double_stack.push1("C")


double_stack.display()

double_stack.push2("a")
double_stack.push2("b")
double_stack.push2("c")

double_stack.display()

double_stack.pop1()
double_stack.pop1()
double_stack.pop1()
double_stack.display()
double_stack.pop2()
double_stack.pop2()
double_stack.pop2()
double_stack.display()
