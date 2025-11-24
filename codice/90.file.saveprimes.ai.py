def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**2**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []

while True:
    try:
        num = int(input())
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if num == 0:
        break

    if is_prime(num):
        primes.append(num)

# Save primes to file
with open("primes.txt", "w") as f:
    for p in primes:
        f.write(str(p) + "\n")
