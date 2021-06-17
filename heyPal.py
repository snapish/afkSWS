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
    a = checkItemExistence("./assets/notepaper/", .74, False , 2, False)
    b = checkItemExistence("./assets/notepaper/", .74, True , 2, False)
    print(a)
    print(b)
    #for notepaperPicture in a:
     #   print(a) 
        #print(pag.locateOnScreen(notepaperPicture, grayscale=True, confidence=0.62, region=REGION))
        
    pag.screenshot('poggers.png', (0, 24, 340, 200))
    #x = checkItemExistence('./assets/notepaper/', .58, True, 2, True)
    # while "generator" in str((pag.locateAllOnScreen(x))):
    #   print(pag.locateAllOnScreen(x))
   # print(pag.locateOnScreen('./assets/NoteMe/superdefence.png', grayscale=False, confidence=0.6, region=REGION))




def checkItemExistence(path, conf, gray, matchesRequired, returnFilesList):
    image_list = []  # gets populated with strings of paths to the files. Function returns this if returnFilesList is True
    matches = 0  # matches pag found
    directory = os.listdir(path)  # get all the files in the directory
    for file in directory:  # for each file thats in the directory
        if file.endswith('.png') or file.endswith('.jpg'):  # if its a compatible image
            image_list.append(path + file)  # example: list[0]= "./assets/shark.png"
    for file in image_list:  # after it gets them all, for each one it found
        if pag.locateOnScreen(file, grayscale=gray, confidence=conf, region=REGION):  # if it can find it on screen
            matches += 1  # add it to the matches count
    if matches >= matchesRequired and not returnFilesList:  # if the request had enough matches and the call didnt want an array returned
        return True
    elif not returnFilesList:  # return false if there werent enough matches, and wanted bool response
        return False
    else:
        return image_list  # return the image list



if __name__ == '__main__':
    main()
