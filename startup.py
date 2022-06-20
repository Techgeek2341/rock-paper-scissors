from tkinter.messagebox import OK, YES
import rps
import pyautogui

name = pyautogui.prompt("what is your name?")

startwin=pyautogui.confirm("shall we start game?")

if startwin=="Cancel":
    pyautogui.alert("ok bye")

if startwin=="OK":
    rps.game()