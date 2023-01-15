import matplotlib.pyplot as plt
import numpy as np
from Clock import clock
import Ex4Her, Ex4Lag, Ex4Sam

def f(x):
    return 1 /(1 +9 *x**2)

def f1(x1):
    return eval(Ex4Lag.Lag()[0])

def f2(x2):
    return eval(Ex4Lag.Lag()[1])

def fh(x):
    return eval(Ex4Her.Her())

def s(x):
    slist = eval(Ex4Sam.Sam())
    cond = [[True if (i>=0 and i<2) else False for i in x]]
    cond.append([True if (i>=2 and i<4) else False for i in x])
    cond.append([True if (i>=4 and i<6) else False for i in x])
    cond.append([True if (i>=6 and i<8) else False for i in x])
    cond.append([True if (i>=8 and i<=10) else False for i in x])
    res = sum([cond[i] *slist[i] for i in range(len(cond))])
    return res

@clock
def main():
    x = np.linspace(0,10,200)
    y = f(x)
    y1 = f1(x)
    y2 = f2(x)
    yh = fh(x)
    ys = s(x)
    plt.figure(num=3,figsize=(8,5))
    line1, = plt.plot(x,y,color='red',linewidth=1.0,linestyle='--')
    line2, = plt.plot(x,y1,color='green',linewidth=1.0,linestyle='--')
    line3, = plt.plot(x,y2,color='black',linewidth=1.0,linestyle='--')
    line4, = plt.plot(x,yh,color='blue',linewidth=1.0,linestyle='--')
    line5, = plt.plot(x,ys,color='purple',linewidth=1.0,linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend((line1, line2, line3, line4, line5),['orig fcn','5th Lagr','10th Lagr','Herm','Sample'])

if __name__ == '__main__':
    main()
    plt.show()