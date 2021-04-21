#4.Given threeintegers, print the smallestone.(Threeintegers should be user input).

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

if a<=b and a<=c:
    print(f"{a} is the smallest")
elif b<=a and b<=c :
    print(f"{b} is the smallest")
elif c<=a and c<=b :
    print(f"{c} is the smallest")
    print("The program is over")