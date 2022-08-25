#To find largest of 3 numbers

a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
c= int(input("Enter number 3:"))

if a>b and a>c:
    print("The largest number is:", a)
if b>a and b>c:
    print("The largest number is:",b)
if c>a and c>b:
    print("The largest number is:",c)
