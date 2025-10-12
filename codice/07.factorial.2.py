n = int(input("Enter a non-negative integer: "))
while n < 0:
    n = int(input("Enter a non-negative integer: "))

# Compute factorial using a while loop
fact = 1
for i in range(2, n+1):
    fact *= i

print(fact)