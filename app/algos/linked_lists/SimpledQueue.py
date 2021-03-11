class Empty(Exception):
    pass

class LinkedQueue():
    class _Nodes():
        __slots__ = '_elements', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    def __init__(self):
        self._head = None
        self._tail = None 
        self._size = None 
    
    def __len__(self):
        return self._size 
    
    def is_empty(self):
        return self._size ==0 
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
    
    def enqueue(self, e):
        