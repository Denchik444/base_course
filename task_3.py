from constant import g

time0 = 0
time = 5
SPEED = input('введите начальную скорость ')
X0 = input('введите начальное расположение по Х ')
Y0 = input('введите начальное расположение по Y ')
X = range(0, 5, 1)
Y = range(0, 5, 1)

while time0 <= time:
    X[time0] = X0 + SPEED * time0
    print(X[time0])
    Y[time0] = Y0 + SPEED * time0 - ((g * (time0 ** 2)) / 2)
    print(Y[time0])
    time0 += 1