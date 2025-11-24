def prime(n):
    if n == 2:
        is_prime = True
    elif n == 1 or n % 2 == 0:
        is_prime = False
    else:
        is_prime = True
        i = 3
        while i * i <= n and is_prime:
            if n % i == 0:
                is_prime = False
            i += 2  # skip even numbers

    return is_prime
