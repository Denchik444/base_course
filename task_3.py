import matplotlib.pyplot as plt
import numpy as np

N = float(input('введите количество точек - '))
def ellipse(a=2, b=1):
   x = np.arange(-5, 5, N)
   y = np.arange(-5, 5, N)

   x, y = np.meshgrid(x, y)
   
   fxy = (x**2)/(a**2) + (y**2)/(b**2)
   plt.contour(x, y, fxy, levels=[1])
   plt.axis('equal')
   plt.savefig('fig_task_3.png')

if __name__ == '__main__':
    ellipse()
