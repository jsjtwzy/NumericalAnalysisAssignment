import sympy as sp
import numpy as np
def poly(xvar, xarray):
    res = 1
    for xai in xarray:
        res *= (xvar -xai)
    return res
def main():
    y5 = np.array((1,6,15))
    x5 = np.linspace(0,2,len(y5))
    x = sp.symbols('x')
    num1, dem1, lag5 = [], [], []
    for i in range(len(y5)):
        num1.append(poly(x, x5)/(x -x5[i]))
        dem1.append(num1[i].evalf(subs = {x:x5[i]}))
        lag5.append(y5[i] *num1[i] /dem1[i])
    L5 = 0
    for add in lag5:
        L5 += add
    L5 = sp.simplify(L5)
    print(sp.latex(L5))
    print(L5)
    return str(L5)
main()