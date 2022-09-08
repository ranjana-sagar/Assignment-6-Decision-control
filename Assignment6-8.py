a=int(input("Enter the coefficient of x^2 term:"))
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the constant term:"))
D=b*b-4*a*c
if D<0:
    print("Both roots are imaginary")
elif D==0:
    print("Both roots are equal")
elif D>0:
    print("Both roots are real and distinct")
