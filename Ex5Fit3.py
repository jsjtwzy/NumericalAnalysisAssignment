import numpy as np
import sympy as sp

from Ex5Fit import Fit

n = 3
symbols = ', '.join(['a{}'.format(i) for i in range(n+1)])
a = sp.symbols(symbols)

def cal():
    return str(Fit(a, n))

if __name__ == '__main__':
    Fit(a, n)
    print(Fit(a, n),'\n', sp.latex(Fit(a, n)))