from math import pi


def minimal(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num1


a = float(input())
b = float(input())
U = minimal(a, b)
V = minimal(a * b, a + b)
W = min(U + V ** 2, pi)
print('U=', U, '\nV=', V, '\nW=', W)
