from .hash_map_base import HashMapBase
from exercise1.utils import bitify


class DoubleHashingHashMap(HashMapBase):

    __slots__ = '_q'

    def __init__(self, cap=17, p=109345121, q=13):
        super().__init__(cap=cap, p=p)
        self._q = 13

    def _hash_code(self, x):
        return sum(int(c) * self._prime**k for k, c in enumerate(bitify(x)))

    def _h(self, x):
        return (self._hash_code(x) * self._scale + self._shift) % self._prime % len(self._table)

    def _d(self, x):
        return self._q - self._hash_code(x) % self._q

    def __getitem__(self, k):
        pass

    def __setitem__(self, k, v):
        if self._n > len(self._table) // 2:  # keep load factor <= 0.5
            # resize must be called at the biggest prime in segmented_sieve(len(self._table), 2 * len(self._table) - 1)
            self._resize(2 * len(self._table) - 1)  # number 2^x - 1 is often prime

    def __delitem__(self, k):
        pass

    def __iter__(self):
        pass

    def _bucket_getitem(self, j, k):
        pass

    def _bucket_setitem(self, j, k, v):
        pass

    def _bucket_delitem(self, j, k):
        pass
