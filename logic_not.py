#write a program to determine whether you have attendance to qualify the course
a = int(input("Write the total number of classes held:"))
b = int(input("number of classes you attended:"))
c = round((b/a)*100, 2)
print(str(c)+"%")
if c<75.0:
    print("You failed the course")
else:
    print("You are qualified the course")