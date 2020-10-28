import math
from math import sqrt
import re


def checkInput(num):
    if re.fullmatch(r'^[+-]?(\d*[.])?\d+$', num) or re.fullmatch(r'^[+-]?\d+[.]?$', num):
        return True
    else:
        return False


x1 = input('Enter the coordinate x of the first point: ')
if not checkInput(x1):
    print('Your data is incorrect!')
else:
    x1 = float(x1)
    y1 = input('Enter the coordinate y of the first point: ')
    if not checkInput(y1):
        print('Your data is incorrect!')
    else:
        y1 = float(y1)
        x2 = input('Enter the coordinate x of the second point: ')
        if not (checkInput(x2)):
            print('Your data is incorrect!')
        else:
            x2 = float(x2)
            y2 = input('Enter the coordinate y of the first point: ')
            if not (checkInput(y2)):
                print('Your data is incorrect!: ')
            else:
                y2 = float(y2)
                x3 = input('Enter the coordinate x of the third point: ')
                if not (checkInput(x3)):
                    print('Your data is incorrect!')
                else:
                    x3 = float(x3)
                    y3 = input('Enter the coordinate y of the third point: ')
                    if not (checkInput(y3)):
                        print('Your data is incorrect!')
                    else:
                        y3 = float(y3)
                        side1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                        side2 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
                        side3 = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
                        if (side1+side2)<side3 or (side1+side3)<side2 or (side2+side3)<side1:
                            print('Such triangle doesn\'t exist!')
                        elif math.isclose(side1, side2) or math.isclose(side1, side3) or math.isclose(side2, side3):
                            if math.isclose(side1, side2) and math.isclose(side1, side3) and math.isclose(side2, side3):
                                print('This triangle is equilateral!')#рівносторонній трикутник
                            else:
                                print('This triangle is isosceles!')#рівнобедрений трикутник
                        else:
                            print('This triangle is versatile!')#різносторонній трикутник