import math #Import Math Module
Base = int(input ('Enter the base of a right-angled triangle: '))
Height = int(input('Enter the height of a right of a right-angled triangle: '))
print('Triangle details are as follows: ')
print('Base = ', Base)
print('Height = ', Height)
Hypotenuse = math.sqrt(Base * Base + Height * Height)
print('Hypotenuse =', Hypotenuse)