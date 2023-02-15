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
def Lag(n):
    lagyvalue = Lagy(f)
    xlin = np.linspace(0,10,n+1)
    ylin = lagyvalue(xlin)
    x = sp.symbols('x')
    res = 0
    ##求Lag基函数
    for i in range(len(xlin)):
        num1 = poly(x, xlin)/(x -xlin[i])
        res += ylin[i] *num1 /num1.subs({x:xlin[i]})
    res = sp.simplify(res)
    return str(res),res

if __name__ == '__main__':
    lag5 = Lag(n1)[1]
    lag10 = Lag(n2)[1]    
    print(sp.latex(lag5),'\n',sp.latex(lag10))
    print(lag5,'\n',lag10)