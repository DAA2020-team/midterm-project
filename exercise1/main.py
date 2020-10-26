from data_structures.double_hashing_hash_map import DoubleHashingHashMap
from exercise1.utils import segmented_sieve


def main():
    my_map = DoubleHashingHashMap()

    # All the countries in the world are 195; the largest prime bigger than 195 is 197
    n = 197

    primes = segmented_sieve(1, 197)


if __name__ == '__main__':
    main()
