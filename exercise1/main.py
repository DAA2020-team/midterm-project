from random import shuffle

from iso4217 import Currency as cur

from data_structures.double_hashing_hash_map import DoubleHashingHashMap


def main():
    my_map = DoubleHashingHashMap()

    codes = [currency.code for currency in cur]
    shuffle(codes)

    for code in codes[:70]:
        my_map[code] = code + " value"

    for code in codes[:30]:
        del my_map[code]

    print(my_map)
    print(my_map.get_collisions())


if __name__ == '__main__':
    main()
