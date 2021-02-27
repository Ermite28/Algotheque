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
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Remove first occurence of value """
        for k in range(self._n):
            if self._A[k] == value:
                for i in range(k, self._n - 1):
                    self._A[i] = self._A[i + 1]
                self._A[self._n - 1] = None
                self._n += -1
                return
        raise ValueError("Value not found")

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """ Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def __repr__(self):
        return str(self._A[: self._n])


if __name__ == "__main__":
    # Proceed to your test here
    pass
