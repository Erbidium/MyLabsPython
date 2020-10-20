from math import sqrt

katet1 = float(input("Введіть катет: "))  # введення першого катета
hypotenuse = float(input("Введіть гіпотенузу: "))  # Введення гіпотенузи
katet2 = sqrt(hypotenuse ** 2 - katet1 ** 2)
innerRadius = (katet1 + katet1 - hypotenuse) / 2
print(innerRadius)
