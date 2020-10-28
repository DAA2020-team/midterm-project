from data_structures.avl_tree import AVLTreeMap
from data_structures.double_hashing_hash_map import DoubleHashingHashMap
import currency.utils as utils


class Currency:

    def __init__(self, code):
        if utils.validate_iso_code(code) is False:
            raise ValueError("code is not a valid ISO4217 code")

        self._code = code
        self._denominations = AVLTreeMap()
        self._changes = DoubleHashingHashMap()

    def _raise_ex_if_den_empty(self):
        if self._denominations.is_empty():
            raise ValueError("No denomination present")

    def _raise_ex_if_code_not_valid(self, c):
        if utils.validate_iso_code(c) is False:
            raise ValueError("code is not a valid ISO4217 code")

    def _raise_ex_if_value_not_int_or_float(self, v):
        if type(v) is not float and type(v) is not int:
            raise ValueError("Value must be a float, " + str(type(v)) + " was provided")

    def set_denominations(self, denominations):
        self._denominations = denominations

    def set_changes(self, changes):
        self._changes = changes

    def add_denomination(self, value):
        if value in self._denominations:
            raise ValueError(str(value) + " is already present")
        self._denominations[value] = value
        return

    def del_denomination(self, value):
        del self._denominations[value]

    def min_denomination(self, value=None):
        self._raise_ex_if_den_empty()
        if value is None:
            return self._denominations.find_min()
        v = self._denominations.find_gt(value)
        if v is None:
            raise ValueError("No denomination greater than " + str(value) + " present")
        return v

    def max_denomination(self, value=None):
        self._raise_ex_if_den_empty()
        if value is None:
            return self._denominations.find_max()
        v = self._denominations.find_lt(value)
        if v is None:
            raise ValueError("No denomination smaller than " + str(value) + " present")
        return v

    def next_denomination(self, value):
        self._raise_ex_if_den_empty()
        try:
            _ = self._denominations[value]
            return self._denominations.find_gt(value)
        except KeyError as e:
            raise ValueError(str(value) + " is not a denomination") from e

    def prev_denomination(self, value):
        self._raise_ex_if_den_empty()
        try:
            _ = self._denominations[value]
            return self._denominations.find_lt(value)
        except KeyError as e:
            raise ValueError(str(value) + " is not a denomination") from e

    def has_denominations(self):
        return not self._denominations.is_empty()

    def num_denominations(self):
        return len(self._denominations)

    def clear_denominations(self):
        self._denominations = AVLTreeMap()

    def iter_denominations(self, reverse=False):
        return self._denominations.__iter__() if not reverse else self._denominations.__reversed__()

    def add_change(self, currency_code, change):
        if currency_code == self._code and change != 1:
            raise ValueError("Same currency code implies change equals to 1")
        self._raise_ex_if_value_not_int_or_float(change)
        self._raise_ex_if_code_not_valid(currency_code)

        try:
            _ = self._changes[currency_code]
        except KeyError:
            self._changes[currency_code] = change
            return
        raise ValueError(str(currency_code) + " is already present.")

    def remove_change(self, currency_code):
        self._raise_ex_if_code_not_valid(currency_code)
        try:
            del self._changes[currency_code]
        except KeyError as error:
            raise KeyError("Currency " + str(currency_code) + " not present.") from error

    def update_change(self, currency_code, change):
        self._raise_ex_if_value_not_int_or_float(change)
        self._raise_ex_if_code_not_valid(currency_code)
        self._changes[currency_code] = change

"""
    def copy(self):
        t = Currency(self._code)
        t.set_denominations(self._denominations)
        t.set_changes(self._changes)

    def deep_copy(self):
        c = Currency("" + self._code)
        for e in self._denominations.breadthfirst():
            c._denominations[e.key()] = e.key()
        for ch in self._changes:
            dp_ch = ch.deep_copy()
            c._changes[dp_ch[0]] = dp_ch[1]

"""
cur = Currency("EUR")
cur.add_denomination(1)
cur.add_denomination(3)
cur.add_denomination(5)
cur.add_denomination(7)

cur.del_denomination(3)

print(cur.min_denomination(1))
print(cur.max_denomination(5))

print(cur.next_denomination(7))
print(cur.prev_denomination(1))

print(cur.has_denominations())
print(cur.num_denominations())

cur.clear_denominations()
print()
for i in range(1, 16):
    cur.add_denomination(i*i)

for i in cur.iter_denominations():
    print(i)
for i in cur.iter_denominations(True):
    print(i)

cur.add_change("ZZZ", 10)
cur.add_change("USD", 10)
cur.add_change("ASD", 199)

cur.remove_change("ASD")
cur.add_change("ASD", 19.983475823498572394857902348750931)
cur.add_change("AWD", True)

cur.remove_change("ASD")
cur.remove_change("ZZZ")
