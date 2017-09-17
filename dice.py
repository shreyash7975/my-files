#!/usr/bin/python3
import random
mypos=0
while mypos<101:
	n=input("press r to roll a dice")

	if n=='r':
		r=random.randint(1,6)
		mypos=mypos+r
		print(mypos)
		print(r)
		
	elif mypos==2:
		mypos=34
		print(mypos)
		mypos=34
		mypos=mypos+6
	elif mypos==40:
		mypos=68
		print(mypos)
		mypos=68
		mypos=mypos+6
	elif mypos==74:
	    mypos=74
	    print(mypos)
	    mypos=74
	    mypos=mypos+2
	elif mypos==76:
	    mypos=97 
	    print(mypos)
	    mypos=97
	    mypos=mypos+3
		

	 
