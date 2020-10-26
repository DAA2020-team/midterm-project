from currency import utils
from data_structures.red_black_tree import RedBlackTreeMap


class Currency:

    def __init__(self, code):
        if utils.validate_iso_code(code) is False:
            raise ValueError("code is not a valid ISO4217 code")

        self._code = code
        self._denominations = RedBlackTreeMap()
        self._changes = {}  # todo change to doublehashinghashmap

    def add_denomination(self, value):
        if value in self._denominations:
            raise ValueError(str(value) + " is already present")

        self._denominations[value] = value
        return

    def del_denomination(self, value):
        del self._denominations[value]

    def min_denomination(self, value=None):
        if self._denominations.is_empty():
            raise ValueError("No denomination present")
        if value is None:
            return self._denominations.find_min()
        v = self._denominations.find_ge(value)
        if v is None:
            raise ValueError("No denomination greater than " + str(value) + "present")
        return v


cur = Currency("EUR")
cur.add_denomination(1)
cur.add_denomination(3)
cur.add_denomination(5)
cur.add_denomination(7)

cur.del_denomination(3)

print(cur.min_denomination(0))

