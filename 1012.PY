A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

TRI = (A * C)/2
CIRC =  3.14159 * (C**2)
TRAP = ((A + B)* C) / 2
QUAD = B**2
RETAN = A * B

print('TRIANGULO: %.3F' %TRI)
print('CIRCULO: %.3F' %CIRC)
print('TRAPEZIO: %.3F' %TRAP)
print('QUADRADO: %.3F' %QUAD)
print('RETANGULO: %.3F' %RETAN)
