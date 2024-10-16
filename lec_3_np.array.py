import numpy as np

a = [1, 2, 4]

b = np.array(a) # создание массива из заданного списка

print(type(a))
print(type(b))

print(a * b)
print(a / b)
print(a - b)
print(b ** 0.5)

c = np.append(b, 'good')
print(c)

print(b[-1])
