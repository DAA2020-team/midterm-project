from .hash_map_base import HashMapBase
from exercise1.utils import bitify
from .map_base import MapBase


class DoubleHashingHashMap(HashMapBase):

    __slots__ = '_z', '_q', '_collision_counter'

    _AVAIL = object()  # sentinal marks locations of previous deletions

    # --------------- NESTED _Item CLASS ---------------

    class _Item(MapBase._Item):

        def __str__(self):
            return "{%s: %s}" % (self._key, self._value)

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
        self._collision_counter = 0

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
        """
        Returns the value associated to key k.
        :param k: key to search
        :return: the value associated to k, if k exists
        """
        pass

    def __setitem__(self, k, v):
        j = self._h(k)
        self._bucket_setitem(j, k, v)  # subroutine maintains self._n
        if self._n > self.capacity() // 2:  # keep load factor <= 0.5
            # resize must be called at the biggest prime in segmented_sieve(len(self._table), 2 * len(self._table) - 1)
            self._resize(2 * self.capacity() - 1)  # number 2^x - 1 is often prime

    def __delitem__(self, k):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        return str([str(item) for item in self._table if item is not None])

    def capacity(self):
        return len(self._table)

    def get_collisions(self):
        return self._collision_counter

    # --------------- PRIVATE METHODS ---------------

    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is DoubleHashingHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j  # mark this as first avail
                if self._table[j] is None:
                    return False, firstAvail  # search has failed
            elif k == self._table[j]._key:
                return True, j  # found a match
            j = (j + self._d(k)) % self.capacity()  # keep looking (cyclically)
            self._collision_counter += 1  # collision found. increment counter

    def _bucket_getitem(self, j, k):
        pass

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)  # insert new item
            self._n += 1  # size has increased
        else:
            self._table[s]._value = v  # overwrite existing

    def _bucket_delitem(self, j, k):
        pass
