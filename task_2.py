import matplotlib.pyplot as plt
import numpy as np

N = int(input('введите количество точек - '))
def hyperbola(k=1):

    x = np.arange(0, 10, N)
    y = k/x

    plt.plot(x, y, label='hyperbola')

    plt.axis('equal')

    plt.savefig('fig_task_2.png')

if __name__ == '__main__':
    hyperbola()