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


