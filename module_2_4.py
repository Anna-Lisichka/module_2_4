numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
l = int(len(numbers)) + 1


for j in range(2, l):
    a = int(j)
    def is_prime(x):
        for i in range(2, (x//2)+1):
            if x % i == 0:
                return False
        return True
    if is_prime(a) == True:
        primes.append(a)
    else:
        not_primes.append(a)

print(primes)
print(not_primes)

