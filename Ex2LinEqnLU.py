import numpy as np
import functools as ft
def sum1(L,U,r,j):
    return sum([L[r, k]*U[k, j] for k in range(r)])
def sum2(L,U,r,i):
    return sum([L[i, k]*U[k, r] for k in range(r)])
def main():
    A = np.array(((-0.002, 2, 2), (1, 0.78125, 0), (3.996, 5.5625, 4)))
    b = np.array([0.4, 1.3816, 7.4178])
    n = np.shape(A)[0]
    # 初始化LU
    L = np.eye(n)
    U = np.zeros(np.shape(A))
    ##求LU
    for r in range(n):
        Usum = ft.partial(sum1, L, U, r)
        Lsum = ft.partial(sum2, L, U, r)
        for j in range(r, n):
            U[r, j] = A[r, j] -Usum(j)
        for i in range(r +1, n):
            L[i, r] = (A[i][r] -Lsum(i)) /U[r, r]
    y = np.linalg.solve(L,b)
    x = np.linalg.solve(U,y)
    print('U = \n',U,'\nL = \n', L)
    print(y,'\n',x)
main()