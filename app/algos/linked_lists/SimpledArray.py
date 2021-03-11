class Empty(Exception):
    pass


class LinkedStack:
    class _Nodes:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        """Push element e at the top of the Stack"""
        self._head = self._Nodes(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty:
            raise Empty("Stack is empty")
        return self.head._element

    def pop(self):
        if self.is_empty:
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


if __name__ == "__main__":
    test = LinkedStack()
    test.push("1er")
    test.top()
    test.push("2éme")
    print("pop :", test.pop())
    test.top()
