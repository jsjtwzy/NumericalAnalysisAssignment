import sympy as sp
ab = [1, 3]
def f(x):
    res = 100 /x**2 *sp.sin(10 /x)
    return res
##定义2^k等分矩形公式
def T0(k, T):
    h = abs(ab[1] -ab[0]) /2**k
    yvalue = [f(ab[0] +(2 *i -1) *h) 
              for i in range(1, 2**(k -1) +1)]
    sres = sum(yvalue)
    res = 0.5 *T +(ab[1] -ab[0]) *sres /2**k
    return res
##定义T_m,k递推公式
def Tmk(m ,Tmm1kp1, Tmm1k):
    res = (4**m *Tmm1kp1 -Tmm1k) /(4**m -1)
    return res
def main():
    i = 1
    T0m = [f(ab[0])+f(ab[1])]
    T = [T0m]
    ##Romberg求积法
    while i == 1 or abs(T[i-1][0] -T[i-2][0])>1e-5:
        T0m.append(T0(i,T0m[i-1]))
        T[0] = T0m
        m = 1
        k = i -m
        for m in range(1, i +1):
            if len(T) < m +1:
                T.append([])
            T[m].append(Tmk(m, T[m -1][k +1], T[m -1][k]))
            k = i -m -1
        i = i+1
    res = T[i-1][0]
    print(sp.N(res))
main()