import matplotlib.pyplot as plt
import numpy as np

q = np.pi / 2
def Lissashy(a=1, A=1, B=3, b=1, t=5):
   x = np.arange(-5, 5, 0.01)
   y = np.arange(-5, 5, 0.01)

   x, y = np.meshgrid(x, y)
   
   fxy = A * np.sin(a * t * q)
   plt.contour(x, y, fxy, levels=[1])
   plt.axis('equal')
   plt.savefig('fig_task_1D.png')

if __name__ == '__main__':
    Lissashy()