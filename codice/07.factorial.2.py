val = int(input("Enter a non-negative integer: "))
while val < 0:
    val = int(input("Enter a non-negative integer: "))

# Compute factorial using a while loop
fa = 1
i = val
while i > 1:
    fa *= i
    i -= 1

print(fa)