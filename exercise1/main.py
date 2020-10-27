from data_structures.double_hashing_hash_map import DoubleHashingHashMap
from exercise1.utils import segmented_sieve

from iso4217 import Currency as cur


def main():
    my_map = DoubleHashingHashMap()

    code = "EUR"
    if code not in [currency.code for currency in cur]:
        raise TypeError

    my_map[code] = 42
    my_map._bucket_setitem(12, "USD", 43)
    my_map._bucket_setitem(12, "JPY", 44)

    print(my_map)

    print(my_map.get_collisions())


if __name__ == '__main__':
    main()
