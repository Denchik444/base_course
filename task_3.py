import numpy as np
from constant import g
from math import sin, cos, pi

X0 = 0
Y0 = 0
alpha = 30 * np.pi / 180
V = 1
Vx0 = V * cos(alpha)
Vy0 = V * sin(alpha)

t = np.linspace(0, 20, 1)
X = X0 + Vx0 * t
Y = Y0 + Vx0 * t - g * t ** 2 / 2

coords = np.zeros((3, len(t)))
coords[:, 0] = t[:]
coords[:, 1] = X[:]
coords = np.column_stack((t, X, Y))

# я не понимаю!