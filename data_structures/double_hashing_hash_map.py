from .hash_map_base import HashMapBase
from exercise1.utils import bitify


class DoubleHashingHashMap(HashMapBase):

    __slots__ = '_z', '_q'

    # --------------- CONSTRUCTOR ---------------

    def __init__(self, cap=17, z=92821, p=109345121, q=13):
        """
        Constructor.
        :param cap: Initial capacity of the HashMap
        :param z: Positive prime used for string hashing (default 92821)
        :param p: Positive prime used for MAD (default 109345121)
        :param q: Positive prime used for secondary hash function compression (default 13)
        """
        super().__init__(cap=cap, p=p)
        self._z = z
        self._q = q

    # --------------- UTILITY METHODS ---------------

    def _hash_code(self, x):
        """
        Returns the polynomial hash code for string x
        :param x: string to hash
        :return: hash code of x
        """
        return sum(int(c) * self._z**k for k, c in enumerate(bitify(x)))

    def _h(self, x):
        """
        Primary hash function. Implements MAD compression
        :param x: key to hash
        :return: compressed primary hash code of x in [0, N - 1]
        """
        return (self._hash_code(x) * self._scale + self._shift) % self._prime % self.capacity()

    def _d(self, x):
        """
        Secondary hash function.
        :param x: key to hash
        :return: compressed secondary hash code of x in [1, q - 1]
        """
        return self._q - self._hash_code(x) % self._q

    # --------------- PUBLIC METHODS ---------------

    def __getitem__(self, k):
        pass

    def __setitem__(self, k, v):
        if self._n > len(self._table) // 2:  # keep load factor <= 0.5
            # resize must be called at the biggest prime in segmented_sieve(len(self._table), 2 * len(self._table) - 1)
            self._resize(2 * self.capacity() - 1)  # number 2^x - 1 is often prime

    def __delitem__(self, k):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        pass

    def capacity(self):
        return len(self._table)

    # --------------- PRIVATE METHODS ---------------

    def _bucket_getitem(self, j, k):
        pass

    def _bucket_setitem(self, j, k, v):
        pass

    def _bucket_delitem(self, j, k):
        pass
