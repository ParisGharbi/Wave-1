#Determine and display whether an integer entered by the user is even or odd

#Read integer from user
num = int(input("Enter an integer: "))

#Determine whether it is even or odd by using the remainder operator
if num % 2 == 1:
    print(num, "is odd.")
else:
    print(num, "is even.")