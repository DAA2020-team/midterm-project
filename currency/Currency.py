from data_structures.avl_tree import AVLTreeMap
from data_structures.double_hashing_hash_map import DoubleHashingHashMap
import currency.utils as utils


class Currency:
    __slots__ = '_code', '_denominations', '_changes'

    def __init__(self, code):
        if utils.validate_iso_code(code) is False:
            raise ValueError("code is not a valid ISO4217 code")

        self._code = code
        self._denominations = AVLTreeMap()
        self._changes = DoubleHashingHashMap()

    @staticmethod
    def _raise_ex_if_code_not_valid(c):
        if utils.validate_iso_code(c) is False:
            raise ValueError("code is not a valid ISO4217 code")

    @staticmethod
    def _raise_ex_if_value_not_int_or_float(v):
        if type(v) is not float and type(v) is not int:
            raise ValueError("Value must be a float, " + str(type(v)) + " was provided")

    def _raise_ex_if_den_empty(self):
        if self._denominations.is_empty():
            raise ValueError("No denomination present")

    def get_change(self, currency_code):
        self._raise_ex_if_code_not_valid(currency_code)
        return self._changes[currency_code]

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

    def copy(self):
        t = Currency(self._code)
        t.set_denominations(self._denominations)
        t.set_changes(self._changes)
        return t

    def deep_copy(self):
        c = Currency(self._code)
        for e in self._denominations.breadthfirst():
            c._denominations[e.key()] = e.key()
        for ch in self._changes:
            c._changes[ch[0]] = ch[1]
        return c
