import numpy as np
import sympy as sp

rho = 1
n = 4
x, a0, a1, a2, a3, a4 = sp.symbols('x, a0, a1, a2, a3, a4')
a = [a0, a1, a2, a3, a4]

# 待定系数构造多项式族
def phi(n):
    res = 0
    for i in range(n +1):
        if i == n:
            res = res +x**i
        else:
            res = res +a[i] *x**i
    return res

# 定义内积
def innerp(f1, f2):
    prod = rho *f1 *f2
    res = sp.integrate(prod,(x,0,1))
    return res

def dinnerp(y1, y2):
    res = 0
    for i in range(len(y2)):
        prod = rho *y1[i] *y2[i]
        res = res +prod
    return res

def Fit():
    eqns = []
    for i in range(n +1):
        for j in range(i):
            eqns.append(innerp(phi(j),phi(i)))
    # 求解系数
    res = [list(sp.solve(eqns[int((i**2 +i)/2):int((i**2 +3 *i +2)/2)], a[:i +1], dict=True)[0].values())\
        +[1] +(n -1 -i) *[0] for i in range(n)]
    # 正交多项式组系数矩阵
    A = np.array([[1,0,0,0,0],*res])
    xp = np.array([1,x,x**2,x**3,x**4])
    Phi = np.matmul(A,xp)
    # 待定系数求拟合多项式
    xserial = np.array([0,0.1,0.2,0.3,0.5,0.8,1])
    yserial = np.array([1,0.41,0.50,0.61,0.91,2.02,2.46])
    Phik = np.zeros((n+1,7))
    for i in range(n +1):
        Phik[i] = np.array([Phi[i].evalf(subs ={x:xj}) 
                    for xj in xserial])
    global phix
    phix = np.matmul(Phi,a)
    phixs = [phix.evalf(subs = {x:xi}) 
             for xi in xserial]
    eqns = [dinnerp(phixs, Phiki) -dinnerp(yserial, Phiki) 
            for Phiki in Phik]
    # 求解线性方程组
    res = sp.solve(eqns,a)
    phix = phix.evalf(subs = res)
    return str(phix)

if __name__ == '__main__':
    Fit()
    print(phix,'\n', sp.latex(phix))