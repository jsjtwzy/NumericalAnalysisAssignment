import sympy as sp
def f1(x):
    return (1 -sp.cos(x)) /x**2
def f2(x):
    return 0.5 *(sp.sin(0.5 *x) /(0.5 *x))**2
def main():
    x = 1.2e-5
    y1 = f1(1.2e-5)
    y2 = f2(1.2e-5)
    print(y1, y2, sp.sin(0.5 *x) /(0.5 *x))
main()