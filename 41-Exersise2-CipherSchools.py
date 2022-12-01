# Exercise - Watch coco
# Ask user's name and age
# if user's name start with ("a" or "A") and age is above 10 then
# print "you can watch coco movie"
# Else print "Sorry,you cannot watch coco"

username=input("Enter your name: ")
age=int(input("Enter your age: "))
if age >= 20 and (username[0] == "a" or username[0] == "A"):
    print("you can watch coco movie")
else:
    print("sorry, you cannot watch coco")    