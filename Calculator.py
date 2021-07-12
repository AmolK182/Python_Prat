print("Enter Number 1 for operation")
a=float(input())
print("Enter Number 2 for operation")
b=float(input())
print("Select operation")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")
print("5 for Remainder")
i=int(input())
if (i==1):
    print(a+b)
elif(i==2):
    print(a-b)
elif(i==3):
    print(a*b)
elif(i==4):
    print(a/b)
elif(i==5):
    print(a%b)
