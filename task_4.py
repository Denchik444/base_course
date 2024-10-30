import numpy as np
from math import sin

N = int(input('введите '))
M = int(input('введите '))
i = 1
j = 1

trigonometry_array = np.linspace(N, M, 1)

trigonometry_array[i, j] = sin(N * i + M * j + 1)

