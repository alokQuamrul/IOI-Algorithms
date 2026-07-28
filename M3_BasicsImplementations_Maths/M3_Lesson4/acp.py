#implement a binary code to convert from Binary number to Decimal number

# ================================
# BINARY TO DECIMAL CONVERTER
# ================================

binary_number = "101101"

print("================================")
print("BINARY TO DECIMAL CONVERTER")
print("================================")
print("Binary Number:", binary_number)

decimal_number = 0
power = 0

# Read the binary digits from right to left.
# Each digit is multiplied by 2 raised to its position power, then summed.
for digit in reversed(binary_number):
    bit = int(digit)
    decimal_number += bit * (2 ** power)
    power += 1

print("Decimal Number:", decimal_number)
print("================================")
