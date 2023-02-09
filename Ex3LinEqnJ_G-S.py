import numpy as np

def split(A):
    D = np.diag(np.diag(A))
    L = np.zeros(np.shape(A))
    for i in range(1, np.shape(A)[0]):
        for r in range(i):
            L[i, r] = A[i, r]
    U = A -D -L
    Res = [L, D, U]
    return Res

def solve(B, b):
    x = np.matmul(B, np.zeros((3,1))) +b
    n = 1
    while np.linalg.norm(np.matmul(B, x) +b -x)>=1e-5:
        x = np.matmul(B, x) +b
        n += 1
    print(x,n)
    
def main():
    A = np.array(((10, -1,0),(-1, 10, -2),(0, -2, 10)))
    b = np.array((9,7,6))
    L = np.array(split(A)[0])
    D = np.array(split(A)[1])
    U = np.array(split(A)[2])
    BJ = np.eye(np.shape(A)[0]) -np.matmul(np.linalg.inv(D), A)
    bj = np.matmul(np.linalg.inv(D), b)
    BG = -np.matmul(np.linalg.inv(L +D), U)
    bg = np.matmul(np.linalg.inv(L +D), b)
    solve(BJ, bj)
    solve(BG, bg)
    
main()