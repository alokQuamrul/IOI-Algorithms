#implement a python code to find out the LCM(Least Common Multiple) of a number

# ================================
# LCM (LEAST COMMON MULTIPLE) FINDER
# ================================

num1 = 4
num2 = 6

print("================================")
print("LCM FINDER")
print("================================")
print("Number 1:", num1)
print("Number 2:", num2)

# The LCM is always divisible by the larger of the two numbers,
# so start checking multiples from there.
greater = max(num1, num2)

lcm = greater
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += greater

print("LCM:", lcm)
print("================================")
