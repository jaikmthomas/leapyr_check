#Write a Python program that inputs three integers and calculates and prints out their sum. However, if the three numbers are all equal then print out three times their sum.
num1 = int(input("Write first number"))
num2 = int(input("Write second number"))
num3 = int(input("Write third number"))
if num1 == num2 == num3:
    sum = 3*num1
    print(sum)
else:
    sum = num1 + num2 + num3
    print(sum)




