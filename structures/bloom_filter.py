"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any, Iterator
from structures.bit_vector import BitVector
from structures.util import object_to_byte_array

class BloomFilter:
    """
    A BloomFilter uses a BitVector as a container. To insert a given key, we
    hash the key using a series of h unique hash functions to set h bits.
    Looking up a given key follows the same logic, but only checks if all
    bits are set or not.

    Note that a BloomFilter is considered static. It is initialized with the
    number of total keys desired (as a parameter) and will not grow. You
    must decide what this means in terms of allocating your bitvector space
    accordingly.

    You can add functions if you need to.

    *** A NOTE ON KEYS ***
    We will only ever use int or str keys.
    We will not use `None` as a key.
    You might like to look at the `object_to_byte_array` function
    stored in util.py -- This function can be used to convert a string
    or integer key into a byte array, and then you can use the byte array
    to make your own hash function (bytes are just integers in the range
    [0-255] of course).
    """
    PRIME = 100_000_007
    NHASH = 7

    def __init__(self, max_keys: int) -> None:
        # You should use max_keys to decide how many bits your bitvector
        # should have, and allocate it accordingly.
        self._size = 10 * max_keys
        self._data = BitVector()
        self._data.allocate(self._size)
        
        # More variables here if you need, of course
        self._empty = True
    
    def __str__(self) -> str:
        """
        A helper that allows you to print a BloomFilter type
        via the str() method.
        This is not marked. <<<<
        """
        pass

    def hash_code(self, key: Any) -> int:
        """
        Cyclic Shift
        """
        if type(key) is int:
            return key

        if type(key) is str:
            h = 0
            mask = (1 << 32) - 1
            for c in key:
                h = (h << 5 & mask) | (h >> 27)
                h += ord(c)
            return h

        raise Exception("In Bloom Filter hash code, key is neither an int or str")

    def hash(self, key: Any) -> Iterator[int]:
        """
        Compression function with MAD
        """
        y = self.hash_code(key)
        b = [ 2, 3, 5, 7, 11, 13, 17 ]
        a = [ 83, 89, 97, 101, 103, 107, 109 ]
        for i in range(self.NHASH):
            yield ((a[i] * y + b[i]) % self.PRIME) % self._size

    def insert(self, key: Any) -> None:
        """
        Insert a key into the Bloom filter.
        Time complexity for full marks: O(1)
        """
        self._empty = False
        for i in self.hash(key):
            self._data.set_at(i)

    def contains(self, key: Any) -> bool:
        """
        Returns True if all bits associated with the h unique hash functions
        over k are set. False otherwise.
        Time complexity for full marks: O(1)
        """
        for i in self.hash(key):
            if self._data.get_at(i) == 0:
                return False
        return True

    def __contains__(self, key: Any) -> bool:
        """
        Same as contains, but lets us do magic like:
        `if key in my_bloom_filter:`
        Time complexity for full marks: O(1)
        """
        return self.contains(key)

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        return self._empty

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of bits) that the underlying
        BitVector can currently maintain.
        Time complexity for full marks: O(1)
        """
        return self._size
