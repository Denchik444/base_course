import numpy as np


N = int(input('введите '))
M = int(input('введите '))
i = 1
j = 1

trigonometry_array = np.zeros(N, M, 1)
for i in range(N):
  while j in range(M):
    trigonometry_array[i, j] = np.sin(N * i + M * j + 1)
    if trigonometry_array[i, j] < 0:
      trigonometry_array[i, j] = 0
  print(trigonometry_array[i, j])