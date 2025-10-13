val = int(input("Enter a non-negative integer: "))
while val < 0:
    val = int(input("Enter a non-negative integer: "))

# Compute factorial using a while loop
fa = 1
i = 2
while i <= val:
    fa *= i
    i += 1

print(fa)