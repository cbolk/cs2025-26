n = int(input("Enter a non-negative integer: "))
while n < 0:
    n = int(input("Enter a non-negative integer: "))

# Compute factorial using a while loop
fact = 1
i = 2
while i <= n:
    fact *= i
    i += 1

print(fact)