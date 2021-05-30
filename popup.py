from operator import contains
import pyautogui as pag
import random as rand
import keyboard
import cv2
import os
import concurrent.futures
import time
from time import sleep
from tkinter import *
from tkinter import ttk

REGION = (960, 540, 1920, 1080)

aggroPotTimer = ""
sharkTimer = ""
daTimer = ""
noteTimer = ""
areaLootTimer = ""
daBool = False
interfaceBool = False

sharkKey = ""
lootInterfaceKey = ""
aggroPotKey = ""
daKey = ""


def main():
    window = Tk()
    window.title = "Toupin's Spiritual Warrior script"
    window.geometry('500x500')
    window.configure(background="goldenrod")
    daBool = IntVar()
    sharkLabel = Label(window, text="Shark keybind").grid(row=0, column=0)
    sharkTextBox = Entry(window).grid(row=0, column=1)

    lootInterfaceLabel = Label(window, text="Open loot interface keybind").grid(row=1, column=0)
    lootInterfaceTextBox = Entry(window).grid(row=1, column=1)

    aggroPotLabel = Label(window, text="Ovl / aggro pot keybind").grid(row=2, column=0)
    aggroPotTextBox = Entry(window).grid(row=2, column=1)

    # only show/enable this if they check the checkbox
    daLabel = Label(window, text="Dissassemble keybind").grid(row=3, column=0)
    daTextBox = Entry(window).grid(row=3, column=1)

    daCheckbox = ttk.Checkbutton(window, text="Disassemble warpriest and junk", variable=daBool, command=toggleDa).grid(row=4, column=0)

    ttk.Button(window, text="Start", command=takeInputs).grid()
    window.mainloop()


def takeInputs():
    print(daBool)
    pass


def toggleDa():
    print(daBool)


if __name__ == "__main__":
    main()
