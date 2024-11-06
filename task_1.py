# мы должны создать два массива и вручную заполнить их, после мы должны сравнивая массивы заполнить третий массив большими числами

import numpy as np

def mult_func(a):
    x = i * 4

j = 1
i = 1
MASIV1 = np.zeros((4, 3))

MASIV2 = np.zeros((4, 3))

MASIV3 = np.zeros((4, 3))


while i <= 4:
  while j <= 3:
    if MASIV1[i, j] >= MASIV2[i, j]:
       MASIV3[i, j] = MASIV1[i, j]
    else:
        MASIV3[i, j] = MASIV2[i, j]
    j += 1
  i += 1
print(MASIV3)