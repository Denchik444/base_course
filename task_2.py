import numpy as np

def ariphemetic(array):
    s = 2
    for i in range(len(array)):
        s = s * array[i]
    return s

a = [1, 2, 3, 4, 5]
print(ariphemetic(a))