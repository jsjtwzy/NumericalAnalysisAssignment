from math import e
import sympy as sp
import functools as ft
from Clock import clock

def f(x):
    return 2 *x**3 -x -1

def df(xvar):
    x = sp.symbols('x')
    return sp.diff(f(x)).evalf(subs = {x:xvar})

def newton(xvar):
    return xvar -f(xvar) /df(xvar)

def secant(xvar0, xvar1):
    return xvar1 -f(xvar1) *(xvar1 -xvar0) /(f(xvar1) -f(xvar0))

@ft.lru_cache()
def secit(n:int, xvar0, xvar1):
    if n == 1:
        return xvar0
    elif n == 2:
        return xvar1
    else:
        return secant(secit(n-2, xvar0, xvar1), secit(n-1, xvar0, xvar1))

@clock
def main():
    ##二分法
    x0 = -2
    x1 = 2
    i = 0
    while abs(x1 -x0)>1e-4:
        if f(0.5*x0 +0.5*x1) *f(x0)>0:
            x0 = 0.5*x0 +0.5*x1
        else:
            x1 = 0.5*x0 +0.5*x1
        i = i+1
    ##Newton法
    x0 = 0
    i = 1
    while abs(newton(x0) -x0)>1e-4:
        x0 = newton(x0)
        i += 1
    print(i)
    ##割线法
    x0 = 0
    x1 = 2
    i = 2
    mySecit = ft.partial(secit, xvar0=x0, xvar1=x1)
    while abs(mySecit(i) -mySecit(i-1))>1e-4:
        i += 1
    print(i, mySecit(i))
main()