from random import shuffle

from iso4217 import Currency as cur

from data_structures.multi_way_search_tree import MultiWaySearchTree
from exercise2.currency import Currency


def main():
    tree = MultiWaySearchTree()

    codes = [currency.code for currency in cur]
    shuffle(codes)

    currencies = [Currency(code) for code in codes]

    for currency in currencies:
        for d in [1, 5, 2]:
            currency.add_denomination(d)
        tree[currency._code] = currency

    print(tree)
    print(len(tree))


if __name__ == '__main__':
    main()
