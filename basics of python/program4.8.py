Subject1 = float(input("Enter the Marks of Data-Structure: "))
Subject2 = float(input("Enter the Marks of Python: "))
Subject3 = float(input("Enter the Marks of Java: "))
Subject4 = float(input("Enter the Marks of C Programming: "))
Subject5 = float(input("Enter the Marks of CSS: "))
sum = Subject1+Subject2+Subject3+Subject4+Subject5
per = sum/5
print("Total Marks Obtained", sum, "Out of 500")
print("Percentage = ", per )
if per >= 90:
    print("Distinction")
else:
    if per >= 80:
        print ("First class")
    else:
        if per >= 70:
            print("Second Class")
        else:
            if per >= 60:
                print("Pass")
            else :
                print('Fail')