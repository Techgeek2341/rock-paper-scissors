import random
from tkinter.messagebox import OK
from turtle import title
import pyautogui
import os

def game():
    choices=["rock","paper","scissors"]
    computer=random.choice(choices)
    user=input("rock paper or scissors?:")


    if computer==user:
        print("tie")
    
    if(user == "scissors" and computer == "rock") or (user == "paper" and computer == "rock"):
        print("you lose ")
        print("player:", user)
        print("computer:",computer)
        os.exit()

    if(user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock"):
         print("player:", user)
         print("computer:",computer)
         win_box=pyautogui.alert(title="you won",
           button="ok"
         )
         os.exit()
