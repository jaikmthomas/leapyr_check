#Write a Python program that inputs a year from the user and prints out whether it was a leap year or not
#Leap years are years that are divisible by four
year = int(input("enter the year"))
if year%4 == 0:
    print("Entered year is leap year")
else:
    print("Entered year is not a leap year")