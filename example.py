class example:
    def __init__(self, *components):
        x = sum(components)
        self._x = components[0] +x
    @property
    def x(self):
        return self._x
y = example(1,2)
print(y.x)