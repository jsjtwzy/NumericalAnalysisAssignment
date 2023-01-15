import numpy as np
def split(A):
    n = np.shape(A)[0]
    D = np.diag(np.diag(A))
    L = np.zeros(np.shape(A))
    for i in range(1, n):
        for r in range(i):
            L[i, r] = A[i, r]
    U = A -D -L
    Res = [L, D, U]
    return Res
def main():
    A = np.array([[10, -1,0],[-1, 10, -2],[0, -2, 10]])
    b = np.array([[9],[7],[6]])
    n = np.shape(A)[0]
    L = np.array(split(A)[0])
    D = np.array(split(A)[1])
    U = np.array(split(A)[2])
    I = np.eye(n)
    BJ = I -np.matmul(np.linalg.inv(D), A)
    bj = np.matmul(np.linalg.inv(D), b)
    BG = -np.matmul(np.linalg.inv(L +D), U)
    bg = np.matmul(np.linalg.inv(L +D), b)
    n1 = 1
    x0 = np.matmul(BJ, np.zeros((3,1))) +bj
    while np.linalg.norm(np.matmul(BJ, x0) +bj -x0)>=1e-5:
        x0 = np.matmul(BJ, x0) +bj
        n1 += 1
    print(x0,n1)
    n1 = 1
    x0 = np.matmul(BG, np.zeros((3,1))) +bg
    while np.linalg.norm(np.matmul(BG, x0) +bg -x0)>=1e-5:
        x0 = np.matmul(BG, x0) +bg
        n1 += 1
    print(x0,n1)
main()