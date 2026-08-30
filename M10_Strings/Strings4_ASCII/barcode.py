# Program 1: Barcode Price Calculation
barcode = input("Enter the barcode: ")
total_price = 0

for ch in barcode:
    ascii_val = ord(ch)                # get ASCII value
    max_digit = max(str(ascii_val))    # find largest digit in ASCII code
    total_price += int(max_digit)      # add to total

print("Final price:", total_price)