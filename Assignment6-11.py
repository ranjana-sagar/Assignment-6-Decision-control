m=int(input("Enter the month number:"))
l1=[4,6,9,11]
l2=[1,3,5,7,8,10,12]
if m==2:
    print("28 or 29 days feburary")
elif m in l1:
    print('30 days in this month')
elif m in l2:
    print("31 dayas in this month")
else:
    print("Invalid month")
