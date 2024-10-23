from constant import g
#import math as np
import math as np

X0 = 0
Y0 = 0
alpha = 30 *np.pi / 180
V = 1
Vx0 = V * np.cos(alpha)
Vy0 = V * np.sin(alpha)

t = np.linspace(0, 20, 1)
X = X0 + Vx0 * t
Y = Y0 + Vx0 * t - g * t ** 2 / 2

coords = np.zeros((3, len(t)))
coords = np.column_stack((t, X, Y))

# я не понимаю!