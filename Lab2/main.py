import math

x1 = float(input('Enter the coordinate x of the first point: '))
y1 = float(input('Enter the coordinate y of the first point: '))
x2 = float(input('Enter the coordinate x of the second point: '))
y2 = float(input('Enter the coordinate y of the first point: '))
x3 = float(input('Enter the coordinate x of the third point: '))
y3 = float(input('Enter the coordinate y of the third point: '))
side1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
side2 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
side3 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
if (side1+side2)<side3 or (side1+side3)<side2 or (side2+side3)<side1:
    print('Such triangle doesn\'t exist!')
elif math.isclose(side1, side2) or math.isclose(side1, side3) or math.isclose(side2, side3):
    if math.isclose(side1, side2) and math.isclose(side1, side3) and math.isclose(side2, side3):
        print('This triangle is equilateral!')
    else:
        print('This triangle is isosceles!')
else:
    print('This triangle is versatile!')