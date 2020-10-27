from data_structures.double_hashing_hash_map import DoubleHashingHashMap

from iso4217 import Currency as cur


def main():
    my_map = DoubleHashingHashMap()

    code = "EUR"
    if code not in [currency.code for currency in cur]:
        raise TypeError

    """Test of setitem"""
    for code in [currency.code for currency in cur]:
        my_map[code] = code + " value"

    print(len(my_map))
    print("Collisions", my_map.get_collisions())

    """Test of getitem"""
    for code in [currency.code for currency in cur]:
        value = my_map[code]

    print(len(my_map))
    print("Collisions", my_map.get_collisions())

    """Test of delitem"""
    for code in [currency.code for currency in cur]:
        del my_map[code]

    print(len(my_map))
    print("Collisions", my_map.get_collisions())


if __name__ == '__main__':
    main()
