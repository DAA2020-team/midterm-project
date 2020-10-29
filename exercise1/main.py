from data_structures.double_hashing_hash_map import DoubleHashingHashMap
from exercise1.utils import load_primes
from iso4217 import Currency as cur


def main():
    my_map = DoubleHashingHashMap()

    code = "EUR"
    if code not in [currency.code for currency in cur]:
        raise TypeError

    print("""Test of setitem""")
    for code in [currency.code for currency in cur]:
        my_map[code] = code + " value"

    print(len(my_map))
    print("Collisions", my_map.get_collisions())

    print("""Test of getitem""")
    for code in [currency.code for currency in cur]:
        value = my_map[code]

    print(len(my_map))
    print("Collisions", my_map.get_collisions())

    print('EUR' in my_map)

    print(my_map.get('EUR', 'pippo'))
    print(my_map.get('LLL', 'pippo'))
    print(my_map.get('EUR'))
    print(my_map.get('LLL'))

    print("""Test of setdefault""")
    print(my_map.setdefault('EUR','paperino'))
    print(my_map['EUR'])
    print(my_map.setdefault('LLL', 'paperino'))
    print(my_map['LLL'])
    print(my_map.setdefault('EUR'))
    print(my_map['EUR'])
    print(my_map.setdefault('MMM'))
    print(my_map['MMM'])

    print("""Test of pop""")
    print(my_map.pop('MMM', 'pluto'))
    print(my_map.pop('LLL'))
    print(my_map.pop('LLL', 'pluto'))
    print(my_map.pop('LLL'))

    print("""Test of popitem""")
    print(my_map.popitem())
    """
        my_map2 = DoubleHashingHashMap()
        my_map2.popitem()
        """

    print("""Test of keys""")
    print(my_map.keys())
    print(len(my_map) == len(my_map.keys()))

    print("""Test of values""")
    print(my_map.values())
    print(len(my_map) == len(my_map.values()))

    print("""Test of items""")
    print(my_map.items())
    print(len(my_map) == len(my_map.items()))

    print("""Test of clear""")
    my_map.clear()
    print(my_map)
    print(len(my_map))

    print("""Test of equals""")
    my_map3 = DoubleHashingHashMap()
    for code in [currency.code for currency in cur]:
        my_map[code] = code + " value"
        my_map3[code] = code + " value"
    print(my_map == my_map3)
    my_map3.popitem()
    print(my_map == my_map3)

    print("""Test of update""")
    my_map3.update(my_map)
    print(my_map == my_map3)
    print(len(my_map) == len(my_map3))

    print("Test of delitem")
    for code in [currency.code for currency in cur]:
        del my_map[code]

    print(len(my_map))
    print("Collisions", my_map.get_collisions())

    print("""Test of load primes""")
    print(load_primes()[:100])


if __name__ == '__main__':
    main()
