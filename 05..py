a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\n--- 1. BASIC SHIFT OPERATORS ---")
# Direct shifts
print("Left Shift (a << b):", a << b)
print("Right Shift (a >> b):", a >> b)

print("\n--- 2. BITWISE LOGIC VIA SHIFTS ---")
# To look at a specific bit using shifts, we shift it to the very edge (position 0)
# and check if it is odd (ends in 1) or even (ends in 0).

# Get the first bit (index 0) of both numbers using right shift
bit_a = (a >> 0) % 2
bit_b = (b >> 0) % 2

print("First bit of a is:", bit_a)
print("First bit of b is:", bit_b)

# Simulate Bitwise AND: Both bits must be 1
bit_and = bit_a * bit_b
print("Simulated AND of first bits:", bit_and)

# Simulate Bitwise OR: At least one bit must be 1
bit_or = 1 if (bit_a + bit_b > 0) else 0
print("Simulated OR of first bits:", bit_or)

# Simulate Bitwise XOR: Bits must be different
bit_xor = 1 if (bit_a != bit_b) else 0
print("Simulated XOR of first bits:", bit_xor)