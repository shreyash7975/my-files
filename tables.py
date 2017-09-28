#! /usr/bin/python3
num  = int(input("enter the number : "))
#number defines multiple number
for  i in range (1,4):
#i is the rangewhich is the table
	for j in range (1,11):
#j is the range from 1 to 10 
		print (i,"x",j,"=",i*j)
#*is multiplication
