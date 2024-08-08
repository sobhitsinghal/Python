sales = float(input('enter total sales of the month '))
if sales >= 100000:
    basic = 4000
    hra = 20 * basic/100
    da = 110 * basic/100
    incentive = sales * 10/100
    bonus = 1000
    conveyance = 500
else:
     basic = 4000
     hra = 10 * basic/100
     da = 110 * basic/100
     incentive = sales * 4/100
     bonus = 500
     conveyance = 500

     salary = basic + hra + da + incentive + bonus + conveyance
     print('Salary Receipt of employee ')
     print('total sales = ', sales)
     print('Basic = ', basic)
     print('HRA = ', hra)
     print('DA = ', da)
     print('Incentive ', incentive)
     print('Bonus = ', bonus)
     print('Conveyance = ', conveyance)
     print('Grass salary = ', salary)
     

           
           
