import pyautogui as pag
import random as rand
import keyboard
import cv2
import os
import concurrent.futures
import time
from time import sleep

REGION = (960, 540,1920,1080 )

def main():
  print(checkItemExistence('./assets/da/', .7, True, 1, True ))
  #  print(pag.screenshot('pee.png', region=(960, 540,1920,1080 )))

def checkItemExistence(path, conf, gray, matchesRequired, returnFilesList):
    image_list = []
    matchedImages = []
    matches = 0
    directory = os.listdir(path)  # './notepaper'
    for file in directory:
        if file.endswith('.png') or file.endswith('.jpg'):
            image_list.append(path + file)

    for file in image_list:
        if pag.locateOnScreen(file, grayscale=gray, confidence=conf, region=REGION) is not None:
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
    