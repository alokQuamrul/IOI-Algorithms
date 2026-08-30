# 01-head-tail.py
# Topic: The Head-Tail Pattern, Base Case for Lists

input("Head-tail - head is lst[0]  tail is lst[1:]  base case is [].  Press Enter ")
print("  [10, 20, 30]  head:", [10, 20, 30][0], "  tail:", [10, 20, 30][1:])
print("  [5, 15, 25]   head:", [5, 15, 25][0],  "  tail:", [5, 15, 25][1:])

lst = [int(x) for x in input("Enter 3 numbers separated by spaces: ").split()]
guess = input("What is the head of " + str(lst) + "? ")
input("Head is lst[0]  tail is lst[1:].  Press Enter ")
print("  head:", lst[0], "  your guess:", guess)