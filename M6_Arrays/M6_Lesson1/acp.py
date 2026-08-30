#Given an array, reverse the array and print it.

# Method 1: Using slicing
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]
print("Reversed array:", reversed_arr)

# Method 2: Using reverse() method
arr2 = [10, 20, 30, 40, 50]
arr2.reverse()
print("Reversed array:", arr2)

# Method 3: Using a loop
arr3 = [100, 200, 300, 400, 500]
n = len(arr3)
reversed_arr3 = []
for i in range(n-1, -1, -1):
    reversed_arr3.append(arr3[i])
print("Reversed array:", reversed_arr3)

