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


def main():
    window = Tk()
    window.title = "Toupin's Spiritual Warrior script"
    window.geometry('500x500')
    window.configure(background="goldenrod")
    ttk.Button(window, text="Yo").grid()
    window.mainloop()
    #x = checkItemExistence('./assets/notepaper/', .58, True, 2, True)
    # while "generator" in str((pag.locateAllOnScreen(x))):
    #   print(pag.locateAllOnScreen(x))
   # print(pag.locateOnScreen('./assets/NoteMe/superdefence.png', grayscale=False, confidence=0.6, region=REGION))


def checkItemExistence(path, conf, gray, matchesRequired, returnFilesList):
    image_list = []
    matchedImages = []
    matches = 0
    directory = os.listdir(path)  # './assets/'
    for file in directory:
        if file.endswith('.png') or file.endswith('.jpg'):
            image_list.append(path + file)

    for file in image_list:
        if pag.locateOnScreen(file, grayscale=gray, confidence=conf, region=REGION):
            matches += 1
            matchedImages.append(path + file)

    if matches >= matchesRequired:
        if returnFilesList:
            return matchedImages
        return True
    else:
        return False


if __name__ == '__main__':
    main()
