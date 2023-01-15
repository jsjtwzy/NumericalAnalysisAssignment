import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 *x**3 -x -1

def main():
    x = np.linspace(-10,10,200)
    y = f(x)
    plt.figure(num=4,figsize=(8,5))
    line1, = plt.plot(x,y,color='red',linewidth=1.0,linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()

main()