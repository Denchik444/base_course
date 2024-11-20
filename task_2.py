import matplotlib.pyplot as plt
import numpy as np

N = float(input('введите количество точек - '))
def hyperbola(k=1):

    x = np.arange(1, 10, N)
    y = k/x
    Nx = np.arange(-10, -1, N)
    Ny = k/Nx
    plt.plot(x, y, label='hyperbola')
    plt.plot(Nx, Ny, label='hyperbola')
    plt.savefig('fig_task_2.png')

if __name__ == '__main__':
    hyperbola()