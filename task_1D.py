a = int(input())
b = int(input())
c = int(input())
# ax^2 + bx + c = 0

D = b**2 - 4*a*c
if D > 0:
    x1 = (-b  + (D) ** 0.5)/(2 * a)
    x2 = (-b  - (D) ** 0.5)/(2 * a)
    print(x1)
    print(x2)
elif D < 0:
    x1 = (-b  + (D) ** 0.5)/(2 * a)
    print(x1)
else:
    print('NO!')