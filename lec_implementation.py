import matplotlib.pyplot as plt
import numpy as np


def circle(R=10):
    x = np.arange(-20, 20, 0.1)
    y = np.arange(-20, 20, 0.1)
   # x = np.arange(-2*R, 2*R, 0.1)
   # y = np.arange(-2*R, 2*R, 0.1)

    # переход к заданным кординатам
    x, y = np.meshgrid(x, y)

    fxy = x**2 + y**2 - R**2 # уравнеие круга

    # команда рисования
    plt.contour(x, y, fxy, levels=[0, 1, 2])
    plt.axis('equal')

    plt.savefig('fig_4.png')

if __name__ == '__main__':
    circle()