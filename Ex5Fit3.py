import numpy as np
import sympy as sp

from Ex5Fit import Fit

rho = 1
n = 3
para = ', '.join(['a{}'.format(i) for i in range(n+1)])
symbols = 'x, ' +para
x, *a = sp.symbols(symbols)

xserial = np.array((0,0.1,0.2,0.3,0.5,0.8,1))
yserial = np.array((1,0.41,0.50,0.61,0.91,2.02,2.46))

def cal():
    return str(Fit(a, n))

if __name__ == '__main__':
    Fit(a, n)
    print(Fit(a, n),'\n', sp.latex(Fit(a, n)))