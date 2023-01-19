import itertools
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
    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(*[a +b for a, b in pairs])
y = Vector(1,2)
print(y.dim)