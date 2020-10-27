from math import floor, sqrt


def bitify(s):
    return ''.join(format(c, 'b') for c in bytearray(s, 'utf-8'))


def simple_sieve(limit, primes):
    """Finds all primes smaller than limit using simple sieve of eratosthenes. It stores found primes in list prime."""
    mark = [False] * (limit + 1)

    for i in range(2, limit + 1):
        if not mark[i]:

            # If not marked yet,
            # then its a prime
            primes.append(i)
            for j in range(i, limit + 1, i):
                mark[j] = True

def primes_in_range(low, high):
    """
    Returns a list containing all primes between start and stop included.
    It is an implementation of Sieve of Eratosthenes algorithm:
    https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html"

    Let R be high and L be low.
    Time complexity is O((R−L+1) * log(log(R)) + sqrt(R) * log(log(sqrt(R))))
    """
    limit = floor(sqrt(high)) + 1
    primes = list()
    simple_sieve(limit, primes)

    n = high - low + 1

    mark = [False] * (n + 1)

    for i in range(len(primes)):
        loLim = floor(low / primes[i]) * primes[i]
        if loLim < low:
            loLim += primes[i]
        if loLim == primes[i]:
            loLim += primes[i]
        for j in range(loLim, high + 1, primes[i]):
            if j != primes[i]:
                mark[j - low] = True

    return [i for i in range(low, high + 1) if not mark[i - low]]
