#  по умолчанию: start = 0, step = 1
# range (start, stop, step)

a = range(0, 10, 2)
print(a)
print(type(a))
print(a[3])

a = 'good'
for i in range(0, 10, 1):
    if i < len(a):
        print(a[i] + ' - Bad')
    else:
        print(f'{i}' + ' - Good')