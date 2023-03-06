#Name: Diyora Alimukhamedova
#Email: diyora.alimukhamedova14@myhunter.cuny.edu
#Date: March 5, 2023
#This program displays a list

items = input("Enter a list of names, seperated by semicolons: ")
items2 = items.split(";")
for name in items2:
    first_last = name.split(",")
    first = first_last[0]
    last = first_last[1]
    print(first, last[1] + ".")

#for i in items:
#    print(i)