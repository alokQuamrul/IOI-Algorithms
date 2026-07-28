#Write a python program to find all the prime numbers having 2 digits.

# ================================
# 2-DIGIT PRIME NUMBER FINDER
# ================================

print("================================")
print("2-DIGIT PRIME NUMBER FINDER")
print("================================")

two_digit_primes = []

for number in range(10, 100):
    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        two_digit_primes.append(number)

print("2-Digit Prime Numbers:", two_digit_primes)
print("Total Count:", len(two_digit_primes))
print("================================")
