import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def try1():
    fig, ax = plt.subplots()
    ax.set_xscale('symlog')
    ax.set_yscale('symlog')
    v = ax.plot(np.random.randn(20),np.random.randn(20),"P",label = 'aaa')
    v[0].set_linestyle((2, (5, 1)))
    ax.set_title('title?')
    ax.set_xlabel('this is x label')
    ax.text(0, 0, r'$\mu=115,\ \sigma=15$')
    ax.annotate('annot',xy= (0.5,0.5), xytext= (1,1), arrowprops= dict(facecolor= 'black', shrink=0.05))
    ax.legend()
    plt.show()

def try2():
    value = np.load('values.npy')
    values = []
    for i in value:
        if i > 0:
            values.append(i)
    values = np.log2(values)
    print(values)
    fig, ax = plt.subplots()
    ax.hist(values, bins= 30)
    #plt.show()
    plt.savefig('scatter.png')

try2()
