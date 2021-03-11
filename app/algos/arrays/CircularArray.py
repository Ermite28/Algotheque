class Empty(Exception):
    pass


class CircularArray(object):
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._capacity = CircularArray.DEFAULT_CAPACITY
        self._data = [None] * self._capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return a reference to the element at the front of queue without removing it."""
        if self.is_empty():
            raise Empty("Array is empty")
        return self._data[self._front]

    def dequeue(self):
        """Remove and return first reference"""

        if self.is_empty():
            raise Empty("Array is empty")
        answer = self.first()
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size < self._capacity // 4:
            self._resize(self._capacity // 2)
        return answer

    def enqueue(self, e):
        """Add object e to the end of the array"""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        index = (self._front + self._size) % len(self._data)
        self._data[index] = e
        self._size += 1

    def _resize(self, c):
        old = self._data
        self._data = [None] * c
        walk = self._front
        for j in self._capacity:
            self._data[j] = old[walk]
            walk = (walk + 1) % self._capacity
        self._front = 0
        self._capacity = c


if __name__ == "__main__":
    # Perform tests here.
    
    test = CircularArray()
    test.enqueue("A")
    test.enqueue("B")
    print(test.dequeue())
    print(test.first())
