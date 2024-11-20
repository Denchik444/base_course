import numpy as np






def ariphemetic(array):
    s = 0
    for i in range(len(array)):
        s += array[i]
    return s / len(array)

a = [0, 1, 2, 3, 4, 5]
print(ariphemetic(a))
ariphemetic(a)

def ariphemetic(*a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s / len(a)

print(ariphemetic(0, 1, 2, 3, 4, 5))