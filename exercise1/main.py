from data_structures.double_hashing_hash_map import DoubleHashingHashMap

from iso4217 import Currency as cur


def main():
    my_map = DoubleHashingHashMap()

    code = "EUR"
    if code not in [currency.code for currency in cur]:
        raise TypeError

    for code in [currency.code for currency in cur]:
        my_map[code] = code

    print(my_map)

    print(my_map.get_collisions())


if __name__ == '__main__':
    main()
