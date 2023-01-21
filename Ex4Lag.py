import sympy as sp
import numpy as np

def Lagy(f):
    """求函数值数列"""
    return lambda x:np.array(tuple(f(xi) for xi in x))

def f(x):
    return 1 /(1 +9 *x**2)

def poly(xvar, xarray):
    """Lagrange polynomial"""
    res = 1
    for xai in xarray:
        res *= (xvar -xai)
    return res

n1 = 5
n2  = 10
def Lag():
    lagyvalue = Lagy(f)
    x5 = np.linspace(0,10,n1+1)
    y5 = lagyvalue(x5)
    x10 = np.linspace(0,10,n2+1)
    y10 = lagyvalue(x10)
    x1, x2 = sp.symbols('x1,x2')
    num1, num2, dem1, dem2, lag5, lag10 = \
        [], [], [], [], [], []
    ##求5次Lag基函数
    for i in range(len(x5)):
        num1.append(poly(x1, x5)/(x1 -x5[i]))
        dem1.append(num1[i].evalf(subs = {x1:x5[i]}))
        lag5.append(y5[i] *num1[i] /dem1[i])
    ##求10次Lag基函数
    for i in range(len(x10)):
        num2.append(poly(x2, x10)/(x2 -x10[i]))
        dem2.append(num2[i].evalf(subs = {x2:x10[i]}))
        lag10.append(y10[i] *num2[i] /dem2[i])
    global L5, L10
    L5 = 0
    for lagi in lag5:
        L5 += lagi
    L5 = sp.simplify(L5)
    L10 = 0
    for lagi in lag10:
        L10 += lagi
    L10 = sp.simplify(L10)
    return (str(L5), str(L10))

if __name__ == '__main__':
    Lag()
    print(sp.latex(L5),'\n',sp.latex(L10))
    print(L5,'\n',L10)