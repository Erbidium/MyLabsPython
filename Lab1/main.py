from math import sqrt
import re

katet1 = (input('Enter a cathetus: '))
if not (re.fullmatch(r'^[+-]?(\d*[.])?\d+$', katet1) or re.fullmatch(r'^[+-]?\d+[.]?$', katet1)):
    print('Your data is incorrect!')
elif float(katet1) <= 0:
    print('The triangle with such cathetus doesn\'t exist!')
else:
    katet1 = float(katet1)
    hypotenuse = (input('Enter a hypotenuse: '))
    if not (re.fullmatch(r'^[+-]?(\d*[.])?\d+$', hypotenuse) or re.fullmatch(r'^[+-]?\d+[.]?$', hypotenuse)):
        print('Your data is incorrect!')
    elif float(hypotenuse < katet1):
        print('Such right triangle doesn\'t exist!')
    else:
        hypotenuse = float(hypotenuse)
        katet2 = sqrt(hypotenuse ** 2 - katet1 ** 2)
        innerRadius = (katet1 + katet2 - hypotenuse) / 2
        print('The radius of the circle inscribed in this triangle: %.2f' % innerRadius)
