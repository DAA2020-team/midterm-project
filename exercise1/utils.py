from math import sqrt


def bitify(s):
    return ''.join(format(c, 'b') for c in bytearray(s, 'utf-8'))


def segmented_sieve(start: int, stop: int):
    """Returns a list containing all primes between start and stop included.
    It is an implementation of Sieve of Eratosthenes algorithm:
    https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html"

    Let R be stop and L be start.
    Time complexity is O((R−L+1) * log(log(R)) + sqrt(R) * log(log(sqrt(R))))"""
    lim = int(sqrt(stop))
    mark = [False] * (lim + 1)
    primes = []

    for i in range(2, lim + 1):
        if not mark[i]:
            primes.append(i)
            for j in range(i * i, lim + 1, i):
                mark[j] = True

    is_prime = [True] * (stop - start + 1)
    for i in primes:
        for j in range(max(i * i, (start + i - 1) // (i * i)), stop + 1, i):
            is_prime[j - start] = False
    if start == 1:
        is_prime[0] = False

    return is_prime
