from math import pi


def min(num1, num2):
    return num1 if num1 < num2 else num2


a = float(input('Please, enter number a: '))
b = float(input('Please, enter number b: '))
U = min(a, b)
V = min(a * b, a + b)
W = min(U + V ** 2, pi)
print('\nThe results are displayed with an accuracy of three digits:')
print('U=%.3f\nV=%.3f\nW=%.3f' % (U, V, W))
