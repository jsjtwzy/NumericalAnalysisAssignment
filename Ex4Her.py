import sympy as sp
import numpy as np

from Ex4Lag import Lagy, f, poly

n = 3
def Her():
    lagyvalue = Lagy(f)
    xh = np.linspace(0,10,n+1)
    yh = lagyvalue(xh)
    x = sp.symbols('x')
    f2 = sp.diff(f(x),x)
    dyh, num, lag, dlag, her, bher, wher = \
        [], [], [], [], [], [], []
    for i in range(len(xh)):
        dyh.append(f2.subs({x:xh[i]}))
        num.append(poly(x, xh)/(x -xh[i]))
        lag.append(num[i] /num[i].subs({x:xh[i]}))
        dlag.append(sp.diff(lag[i],x))
        her.append((1 -(x -xh[i])*2*dlag[i]) *lag[i] *lag[i])
        bher.append((x -xh[i]) *lag[i] *lag[i])
        wher.append(yh[i] *her[i] +dyh[i] *bher[i])
    global Lh
    Lh = 0
    for wheri in wher:
        Lh += wheri
    Lh = sp.simplify(Lh)
    return str(Lh)

if __name__ == '__main__':
    Her()
    print(sp.latex(Lh))
    print(Lh)