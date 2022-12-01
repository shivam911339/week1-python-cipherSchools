# Ask user input 3 number and you have to print average of three numbers using string formating


#Bonus:-try to take all three comma separated inputs in one line.


A,B,C=(input("Enter number A , B and C ")).split(",")
print(f"average of three numbers{(int(A)+int(B)+int(C))/3}")
