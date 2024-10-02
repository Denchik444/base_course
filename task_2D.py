a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < a + b:
    print('Существует')
else:
    print('NOСуществует')

if a == b and a == c and b == c:
    print('Равностороность')
elif a == b or a == c or b == c:
    print('Равнобедренность')
else:
    print('Никакой!')