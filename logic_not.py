#write a program to determine Grades scored in an exam
a = int(input("Write your score:"))
if a>= 90:
    print("Great job! you got A grade")
elif a<90 and a>=80:
    print("Impressive! you got B grade")
elif a<80 and a>=70:
    print("Good! you got C grade")
elif a<70 and a>=60:
    print("you got D grade, Need to improve")
else:
    print("You are failed! you got E grade")