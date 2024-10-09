znamenatel = int(input())
nachal = int(input())
n = int(input())
don = 1

while don < n + 1:
    sechas = don - 1
    q = znamenatel ** sechas
    bn = nachal * q
    print(bn)
    don += 1
