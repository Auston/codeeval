def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for j in range(2, n):
            if (n % j) == 0:
                return False
        return True

prime_sum = 0
i = 2
count = 0
while True:
    if is_prime(i):
        count += 1
        prime_sum += i
    i += 1
    if count == 1000:
        break

print prime_sum
