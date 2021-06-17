# 10 PRAYER BONUS CALCULATIONS: aers gives 370 points, a prayer renewal gives 454 every 5 mins. Puts us at like -254 prayer points per minute, so 3/5 minutes we can SS
# assume 100 paper/hr
# TODO add mouse bouncing, and randomize kb/m inputs on things like area loot, ovl, etc.
import time
from time import sleep
import random as rand
import pyautogui as pag
import os
import concurrent.futures
import keyboard
import cv2
from popup import window
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QGridLayout, QLineEdit, QLayout

REGION = (0, 24, 340, 200)# (1600, 720, 1920, 1080)
RUNNING = False
PAUSED = False
# get input for a password that md5s against something probably
# md5 things, prompt windows, pyautogui cheat sheet
#shark 30, loot 15, note 35
intervals = {"tc": 10, "da": 15, "aggro": 295, "shark": 25, "loot": 10, "lootInterface": 300, "note": 30}
last = {}

last["tc"] = time.time()
last["da"] = time.time()
last["aggro"] = time.time()
last["shark"] = time.time()
last["loot"] = time.time()
last["interface"] = time.time()
last["note"] = time.time()


sharkKey = "v"  # these will all be prompted variable inputs. For variablity
lootInterfaceKey = "m"
daKey = "8"
aggroKey = "c"
tcKey = "8"

def main():
    startTime = time.time()
    runTime = time.time - time.time()
    app = QApplication(sys.argv)
    widget = QWidget()
    grid = QGridLayout()
    widget.setLayout(grid)
    
    widget.setGeometry(1200, 500, 500, 500)
    widget.setWindowTitle("Grief will be banned in Modern")
    try:
        while RUNNING:
            checkLootInterface(last["interface"])
            invManagement()
            upkeepOverload(last["aggro"])
    except KeyboardInterrupt:
        print('pressed ctrl + c to exit')


def invManagement():
    areaLoot(last["loot"])
    # daJunk(last["da"])
    chompSharks(last["shark"])
    areaLoot(last["loot"])  # force an area loot before noting
    notePotions(last["note"], './assets/NoteMe/superstrength.png')
    notePotions(last["note"], './assets/NoteMe/superattack.png')
    notePotions(last["note"], './assets/NoteMe/superdefence.png')
    


#

# returns true or false based on whether or not it noted pots
# pass last["note"] for a legit check, or pass a number bigger number to force it
# pass file as the path to the super pot image to check against
def notePotions(lastnote, file):
    if time.time() - lastnote > intervals["note"] :  # whenits time to note potions again
        nps = os.listdir("./assets/notepaper") #get all notepaper pictures
        notepaperExists = checkItemExistence("./assets/notepaper/", .60, True, 2, False)
        potionExists = checkItemExistence(file, .70 , False, 1, False)
        notepaperRegion = None
        for np in nps:
            notepaperRegion = pag.locateOnScreen("./assets/notepaper/"+np, grayscale = True, confidence=0.60, region = REGION)
            if notepaperRegion is not None:
                break
        print(notepaperExists, notepaperRegion, potionExists)
        if notepaperExists and notepaperRegion is not None and potionExists: 
            potLocation = pag.locateOnScreen(file, grayscale=False, confidence=0.70, region=REGION)
            pag.moveTo(notepaperRegion, duration=1)
            time.sleep(2)
            adjust(6, 10)
            pag.click()
            print('click notepaper')
            print('pot location: ', potLocation)
            pag.moveTo(potLocation, duration=1)
            adjust(6, 10)
            print('clicked pot', file)
            pag.click()  # add the check for "notepaper ->"
            last["note"] = time.time()
            return True
    return False

#add cooldowns to functions, and figure out why it never sees pots/paper
#add last["x"] = time at the START and then add random delay in the middle/after


# Looks over all the files in the specified path to see if any are valid
# Args: the path ('./notepaper'), the confidence interval (.55), whether or not its grayscale (True),
# matchesrequired is how many matches in the dir it should have to find, returnFilesList is a boolean that changes the return from true to a list of matched images
# .55 and 2 are good for conf and matchesrequired for notepaper i think?
#
def checkItemExistence(path, conf, gray, matchesRequired, returnFilesList):
    image_list = []  # gets populated with strings of paths to the files. Function returns this if returnFilesList is True
    matches = 0  # matches pag found
    pathFlag = True #flag for if they passed a file instead of a directory
    if os.path.isfile(path):
        image_list.append(path)
        pathFlag = False
    else: directory = os.listdir(path)  # get all the files in the directory
    if pathFlag:    
        for file in directory:  # for each file thats in the directory
            if file.endswith('.png') or file.endswith('.jpg'):  # if its a compatible image
                image_list.append(path + file)  # example: list[0]= "./assets/" + "shark.png"
    for file in image_list:  # after it gets them all, for each one it found
        if pag.locateOnScreen(file, grayscale=gray, confidence=conf, region=REGION):  # if it can find it on screen
            matches += 1  # add it to the matches count
    if matches >= matchesRequired and not returnFilesList:  # if the request had enough matches and the call didnt want an array returned
        return True
    elif not returnFilesList:  # return false if there werent enough matches, and wanted bool response
        return False
    else:
        return image_list  # return the image list


# remember to do after cuz pots are worth more
def chompSharks(lastshark):
    count = 0
    if time.time() - lastshark > intervals["shark"]:
        # go until all the sharks are chompt, or you've gone thru 5 times cuz then somethings probably wrong
        while checkItemExistence('./assets/', .6, False, 1, False):
            print('press shark key')
            keyboard.press(sharkKey)
            count += 1
            if count > 3:
                break
            sleep(rand.uniform(1.2, 1.7))  # hang out for a tick or two
        last["shark"] = time.time()
# done

def targetCycle(lastTc):
    if time.time() - lastTc > intervals["tc"]: #after 5 sec tc
        keyboard.press_and_release(tcKey)
        print('pressed shift+space to area loot')
        last["tc"] = time.time()
        return True
    else:
        return False

def areaLoot(lastloot):
    if time.time() - lastloot > intervals["loot"]:
        rs()
        keyboard.press_and_release('shift + space')
        print('pressed shift+space to area loot')
        last["loot"] = time.time()
        return True
    else:
        return False

# done
# checks overload timer, and if its been long enough, waits a random few seconds then drinks and updates time


def upkeepOverload(lastovl):
    if time.time() - lastovl > intervals["aggro"]:
        rs()
        print('drank overload')
        keyboard.press(aggroKey)
        last["aggro"] = time.time()
        return True
    else:
        return False

# done
# see if its been a while since we re-openeed the loot interface, then press the loot interface key if it has


def checkLootInterface(lastinterface):
    if time.time() - lastinterface > intervals["lootInterface"]:
        rs() # sleep for a random amount of ms
        print('opened loot interface')
        keyboard.press(lootInterfaceKey)
        last["interface"] = time.time()
        return True
    else:
        return False

# yikes
# dissassembles anything inside the da folder, repeats until its all gone


def daJunk(lastda):
    if time.time() - lastda > intervals["da"] + rand.randrange(5, 10) and checkItemExistence('./assets/da/', .6, True, 1, False) :
        daList = checkItemExistence('./assets/da/', .6, True, 1, True)
        for itemToDa in daList:
            rs()
            print('press da key')
            #keyboard.press(daKey)###
            print('about to move to ', itemToDa)
            moveTo = pag.locateOnScreen(itemToDa, grayscale=False, confidence=.6, region=REGION)
            pag.move(moveTo, duration=1)
            adjust(4, 6)
            #pag.click()
            print('clicked junk')
    last["da"] = time.time()


def rs():
    time.sleep(rand.uniform(2.0, 6.0))


# x and y are the offsets on the respective axies
def adjust(x, y):
    x = rand.randrange(0, x)
    y = rand.randrange(0, y)
    pag.moveRel(x, y) #check if i can do this with negatives


if __name__ == '__main__':
    #if window():
   main()
