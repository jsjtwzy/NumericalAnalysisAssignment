
import numpy as np
def main():
    # 输入系数矩阵
    A = np.array(((-0.002, 2, 2), (1, 0.78125, 0), (3.996, 5.5625, 4)))
    b = np.array((0.4, 1.3816, 7.4178))
    n = np.shape(A)[0]
    P = np.eye(n)
    # Gauss消元
    for j in range(n):
        for i in range(j, n):
            # 选取列主元
            if abs(A[j][j])<abs(A[i][j]):
                c = b[j].copy()
                d = A[j].copy()
                b[j], b[i], A[j], A[i] = b[i], c, A[i], d
        # 消元
        for i in range(j +1, n):
            P[i] = P[i]-A[i][j] /A[j][j]*P[j]
            A[i] = A[i]-A[i][j] /A[j][j]*A[j]
    # 对b进行相同变换
    b = np.matmul(P,b.T)
    # 求解方程
    y = np.linalg.solve(A,b)
    print(A,b,y)
main()