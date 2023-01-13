#write a program to determine that a person is an adult (18+) or a minor
num = int(input("Write your age:"))

if num < 18:
    print("you are a minor")
elif num >= 18:
    print("you are an adult")