from math import sqrt

katet1 = float(input("Введіть катет: "))  # Введення першого катета
hypotenuse = float(input("Введіть гіпотенузу: "))  # Введення гіпотенузи
katet2 = sqrt(hypotenuse ** 2 - katet1 ** 2)  # Обчислення другого катета
innerRadius = (katet1 + katet2 - hypotenuse) / 2  # Обчислення радіса кола, вписаного у цей прямокутний трикутник
print("Радіус кола, вписаного у цей трикутник: %.3f" % innerRadius)  # Виведення обчисленого радусу на екран
