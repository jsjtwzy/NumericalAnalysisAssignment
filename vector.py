import itertools
import numbers
import math
class Vector:
    def __init__(self, *components):
        dim = len(components)
        self._dim = dim
        self._components = components
    
    @property
    def dim(self):
        return self._dim
    def __iter__(self):
        return iter(self._components)
    def __repr__(self):
        return 'Vector' +str(self._components)
    
    #reload operators
    def __neg__(self):
        return Vector(*[-a for a in self._components])
    def __pos__(self):
        return self
    def __abs__(self):
        return math.sqrt(self @self)
    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(*[a +b for a, b in pairs])
    def __radd__(self, other):
        return self +other
    def __sub__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(*[a -b for a, b in pairs])
    def __rsub__(self, other):
        return other -self
    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(*[scalar *a for a in self._components])
        else:
            return NotImplemented
    def __rmul__(self, scalar):
        return self *scalar
    def __matmul__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return sum([a *b for a, b in pairs])
    def __rmatmul__(self, other):
        return self @other

y = abs(-Vector(1, 2)) *Vector(1, 3)
print(y)