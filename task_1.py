import numpy as np


N = int(input('введите количество '))

MASS1 = np.arange(0, 100, N)
print(MASS1)

MASS2 = np.arange(0, 100, N)
print(MASS2)

MASS3 = np.arange(0, 100, N)
print(MASS3)

W = 
for i in range(len(N)):
    
        W += N[i]



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