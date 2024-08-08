num = int(input('enter the number: '))
print('entered number is: ', num)
if(num % 5 == 0 and num % 10 == 0):
    print(num, 'is divisible by both 5 and 10 ')
    if(num % 5 == 0 or num % 10 == 0):
        print(num, 'is divisible by 5 or 10')
    else:
        print(num, 'is not divisible by either of them ')