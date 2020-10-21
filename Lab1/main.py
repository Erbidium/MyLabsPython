from math import sqrt

katet1 = float(input("Введіть катет: "))
if katet1<=0:
    print("Трикутник с таким катетом не існує")
else:
    hypotenuse = float(input("Введіть гіпотенузу: "))
    if hypotenuse<katet1:
        print("Такий прямокутний трикутник не існує")
    else:
        katet2 = sqrt(hypotenuse ** 2 - katet1 ** 2)
        innerRadius = (katet1 + katet2 - hypotenuse) / 2
        print("Радіус кола, вписаного у цей трикутник: %.2f" % innerRadius)