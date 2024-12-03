import matplotlib.pyplot as plt
import numpy as np

def polari(b=1, k=2):
   fi = np.arange(0, 8*np.pi, 0.1)
   r = k * fi
   x = r * np.cos(fi)
   y = r * np.sin(fi)

   
   
   
   plt.contour(x, y, levels=[1])
   
   plt.savefig('fig_task_4.png')

if __name__ == '__main__':
    polari()

