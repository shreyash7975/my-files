#! /usr/bin/python3
import random
count=0
r=0
while count<=100:
	roll=input("press r to roll the dice")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("your random num is",r)
		print("you are on count",count)
	elif count=="8":
		count=37
		print("you club the ladder",count)
	if count=="40":
		count=68
		print("you club the ladder",count)
	elif count=="76":
		count=97
		print("you club the ladder",count)
	if count=="11":
		count=2
		print("down the ladder",count)

