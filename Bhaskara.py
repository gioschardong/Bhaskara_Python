import math
print('Insira o valor de A: ', end='')
A = float(input())

print('Insira o valor de B: ', end='')
B = float(input())

print('Insira o valor de C: ', end='')
C = float(input())

Delta = ((B*B)-(4*A*C))

if A == 0:
    print("O valor de a, deve ser diferente de 0")
elif Delta < 0:
    print("Sem raízes reais")
else:
    x1 = (- B + math.sqrt(Delta)) / (2*A)
    x2 = (- B - math.sqrt(Delta)) / (2*A)

    print("x1: {:.2f}, x2: {:.2f}".format(x1, x2)) 
