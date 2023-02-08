import sympy as sp
import numpy as np

import functools as ft

from Clock import clock

from Ex4Lag import f

@ft.lru_cache()
def diffquol(f):
    """f的一阶差商"""
    return lambda x1, x2: (f(x1) -f(x2)) /(x1 -x2)

@ft.lru_cache()
def diffquon(*x):
    """n阶差商"""
    xcut = list(set(x))
    a = sp.symbols('a')
    df = lambda x1: sp.diff(f(a), a).subs({a:x1})
    if len(xcut) <3:
        try:
            return diffquol(f)(*xcut)
        except:
            return df(xcut[0])
    else:
        return (diffquon(*xcut[:-1]) -diffquon(*xcut[:-2], x[-1])) /(xcut[-2] -xcut[-1])

n = 5
def Sam():
    mu = 0.5
    lam = 1 -mu
    xs = np.linspace(0,10,n+1)
    A = 2 *np.eye(n-1)
    d = np.ones(n-1)
    for i in range(n-1):
        d[i] = diffquon(xs[i], xs[i+1], xs[i+2])
        if i == 0:
            A[i][i+1] = lam
        elif i == n-2:
            A[i][i-1] = mu
        else:
            A[i][i+1] = lam
            A[i][i-1] = mu
    M = np.linalg.solve(A, 6 *d)
    M = np.array([0]+list(M)+[0])
    x = sp.symbols('x')
    global s
    s = []
    for i in range(n):
        hip1 = xs[i+1] -xs[i]
        p3 = ((xs[i+1] -x)**3 *M[i] +(x -xs[i])**3 *M[i+1]) /6 /hip1
        ai = (f(xs[i+1]) -f(xs[i]) -hip1**2 /6 *(M[i+1] -M[i])) /hip1
        bi = f(xs[i]) -hip1**2 *M[i] /6
        si = sp.expand(p3 +(x -xs[i]) *ai +bi)
        s.append(si)
    return str(s)

if __name__ == '__main__':
    Sam()
    print(s,'\n',sp.latex(s))