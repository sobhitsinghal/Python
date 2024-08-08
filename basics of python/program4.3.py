from math import pi
radius = eval(input("Enter radius of circle: " ))
if radius > 0:
    area = radius * radius *pi
    print("area of circle is =", format(area, ".2f" ))
    circumference = 2 * pi * radius
    print("Circumference of circle is =", format(circumference, ".2f`"))