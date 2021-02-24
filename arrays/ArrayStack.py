class Empty(Exception):
    """ Error attempting to access an element from an empty container """

    pass


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, n):
        """ Add element n to the top of the Stack """
        self._data.append(n)

    def pop(self):
        """ Remove and return the top element from the Stack; an error occurs if the stack is empty """

        if self.is_empty():
            raise Empty("Array is Empty")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("Array is Empty")
        return self._data[-1]

    def is_empty(self):
        """ Return true if the Stack does not contain any element """
        return len(self._data) == 0
