import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return 100 /x**2 *np.sin(10 /x)
def main():
    x = np.linspace(1, 3, 200)
    y = f(x)
    plt.figure(num=3,figsize=(8,5))
    plt.plot(x,y,color='red',linewidth=1.0,linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
main()