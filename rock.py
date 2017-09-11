#! /usr/bin/python3
from random import randint
 

t = ["Rock", "Paper", "Scissors"]
 

computer = t[randint(0,2)]
 

player = False
 
while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "hugs", player)
        else:
            print("You win!", player, "kisses", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "slaps", player)
        else:
            print("You win!", player,"kicks", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
    player = False
    computer = t[randint(0,2)]