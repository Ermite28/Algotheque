"""
Useless in practice, but interesting to understand how the List object is
implemented in Python.
List has a fixed capacity and are dynamically increased when the limit is reached.
"""

import ctypes


class DynamicArray:
    """ A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        """Return an element at index k."""
        if not 0 <= k < self._n:
            raise IndexError("Invalid index")
        return self._A[k]

    def append(self, obj):
        """Add object to the end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A.append(obj)
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(self, c)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """ Return new array with capacity c."""
        return (c * ctypes.py_object)()
