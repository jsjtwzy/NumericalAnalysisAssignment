import itertools
import numbers
import math

class Vector:
    '''Defined a Vector class supports operants.'''
    def __init__(self, *components):
        self._dim = len(components)
        self._components = components
    
    @staticmethod
    def epsilon(i,j,k):
        if (j -i) *(k -j) *(i -k) == -2:
            return 1
        elif (j -i) *(k -j) *(i -k) == 2:
            return -1
        else:
            return 0

    @staticmethod    
    def delta(i, j):
        if i==j:
            return 1
        else:
            return 0
    
    @property
    def dim(self):
        return self._dim
    
    def __iter__(self):
        return iter(self._components)
    def __getitem__(self, index):
        return self._components[index]
    def __repr__(self):
        return 'Vector' +str(self._components)
    
    #reload operators
    def __neg__(self):
        return Vector(*(-a for a in self._components))
    def __pos__(self):
        return self
    def __abs__(self):
        return math.sqrt(self @self)
    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(*(a +b for a, b in pairs))
    def __radd__(self, other):
        return self +other
    def __sub__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(*(a -b for a, b in pairs))
    def __rsub__(self, other):
        return other -self
    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(*(scalar *a for a in self._components))
        else:
            return NotImplemented
    def __rmul__(self, scalar):
        return self *scalar
    def __matmul__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return sum(a *b for a, b in pairs)
    def __rmatmul__(self, other):
        return self @other
    
    @classmethod
    def crossmul(cls, a, b):
        if a._dim <=3 and b._dim <=3:
            aIn = a +Vector(0, 0, 0)
            bIn = b +Vector(0, 0, 0)
            y = [0, 0, 0]
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        y[i] += Vector.epsilon(i, j, k) *aIn[j] *bIn[k]
            return Vector(*y)
        else:
            return NotImplemented
    
    @classmethod
    def cartianmul(cls, a, b):
        return Vector(*itertools.product(a, b))

y = Vector.cartianmul(-Vector(1, 2), Vector(1, 2, 3))
print(y)