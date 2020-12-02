from math import pi


def minimal(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num1


a = float(input('Please, enter number a: '))
b = float(input('Please, enter number b: '))
U = minimal(a, b)
V = minimal(a * b, a + b)
W = min(U + V ** 2, pi)
print('\nU=%.2f\nV=%.2f\nW=%.2f' % (U, V, W))
