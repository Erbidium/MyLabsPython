import math

x = 0.56
e = 0.00001
n = 1
yZn = math.sin(x)
y = 1/yZn
print("Precision is: e=", e)
print("x=", x)
print("y(%-3d)=%0.8f" % (n, y))
while True:
    yPrev = y
    n += 1
    yZn += math.sin(x) * (1 / (n**2))
    y = 1 / yZn
    print("y(%-3d)=%0.8f" % (n, y))
    if not math.fabs(y-yPrev) > e:
        break
print("\nResult:\ny=%0.8f" % y)
