print('Point1')
X1 = eval(input('Enter X1 coordinate: '))
Y1 = eval(input('Enter Y1 coordinate: '))
print('point2')
X2 = eval(input('enter X2 coordinate:'))
Y2 = eval(input('Enter Y2 coordinate: '))
L1 = (X2 - X1)**2 + (Y2 - Y1)**2
Distance = L1**0.5
print('Distance between two point is as follows')
print('(',X1,Y1,')','(',X2,Y2,')=', Distance )