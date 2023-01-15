import matplotlib.pyplot as plt
import numpy as np
from Clock import clock
import Ex5Fit, Ex5Fit3

def f1(x):
    return eval(Ex5Fit.Fit())

def f2(x):
    return eval(Ex5Fit3.Fit())

@clock
def main():
    x = np.linspace(0,1,200)
    xserial = np.array([0,0.1,0.2,0.3,0.5,0.8,1])
    yserial = np.array([1,0.41,0.50,0.61,0.91,2.02,2.46])
    y1 = f1(x)
    y2 = f2(x)
    plt.figure(num=5,figsize=(8,5))
    plt.scatter(xserial,yserial,c='red',s=[10])
    line2, = plt.plot(x,y1,color='green',linewidth=1.0,linestyle='--')
    line3, = plt.plot(x,y2,color='black',linewidth=1.0,linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend((line2, line3),[r'$4^{th} Fit$',r'$3^{th} Fit$'])

if __name__ == '__main__':
    main()
    plt.show()