def changer(a, b):
    a = 2
    b[0] = 'Good'

x = 10
L = [1, 2]

changer(x, L) # changer - изменяет глобальные данные локальными (L[0] = 1 / b[0] = 'Good')

print(x)
print(L)

L = [1, 2]
changer(x, L[:])

print(x)
print(L)

################# комплексные числа ###############

x = 3
y = 4

z = complex(x, y) # вектор
print(z)

w = complex(y, x)
print(z + w)


s = 'hello'
print(s[0])

# s[0] = 'H'
# print(s[0]) - неизменяемая

################### кортедж ##################

t = (1, 4, 9)
print(t)
print(t[0])
# t[0] = 3 - не пощволяет изменять

# листы
l = [1, 4, 9]
l[0] = 3
print(l)

# словари
d = {'al':4, 4:'al', 'str':'Hello'}
print(d['al'])
print(d[4])
print(d['str'])

d['str'] = 'Good'
print(d)