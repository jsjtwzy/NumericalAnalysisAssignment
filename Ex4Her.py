import sympy as sp
import numpy as np

from Ex4Lag import Lagy, f, poly

n = 3
def Her(n):
    lagyvalue = Lagy(f)
    xh = np.linspace(0,10,n+1)
    yh = lagyvalue(xh)
    x = sp.symbols('x')
    f2 = sp.diff(f(x),x)
    global res
    wher = 0
    for i in range(len(xh)):
        dyh = f2.subs({x:xh[i]})
        num = poly(x, xh)/(x -xh[i])
        lag = num /num.subs({x:xh[i]})
        dlag = sp.diff(lag,x)
        her = (1 -(x -xh[i])*2*dlag) *lag *lag
        bher = (x -xh[i]) *lag *lag
        wher += (yh[i] *her +dyh *bher)
    res = sp.simplify(wher)
    return str(res), res

if __name__ == '__main__':
    her = Her(n)[1]
    print(sp.latex(her))
    print(her)