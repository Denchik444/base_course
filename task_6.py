peremennay = 1
peremennay1 = 1


for i in range(0, 9, 1):
    for k in range(0, 9, 1):
      print(peremennay*peremennay1, end='   ')
      peremennay1 = peremennay1 + 1
    print()  
    peremennay = peremennay + 1
    peremennay1 = 1