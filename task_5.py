a = int(input())
b = int(input())

# a == 0 or b == 0

if a != 0 and b != 0:
    if a % b == 0:
       print('делится')
       print(a % b)
       print(a / b)
    else:
       print('NOделится')
       print(a % b)
       print(a / b)
else:
   print('NO NO NO!')