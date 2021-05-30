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
import easygui


REGION = (960, 540, 1920, 1080)
# get input for a password that md5s against something probably
# md5 things, prompt windows, pyautogui cheat sheet
intervals = {"da": 10, "aggro": 290, "shark": 45, "loot": 15, "lootInterface": 300, "note": 25}
last = {"da": 0, "aggro": 0, "shark": 0, "loot": 0, "interface": 0, "note": 0}

sharkKey = "v"  # these will all be prompted variable inputs. For variablity
lootInterfaceKey = "m"
daKey = "8"
aggroKey = "c"


def main():
    try:
        while True:
            checkLootInterface(last["interface"])
            upkeepOverload(last["aggro"])
            invManagement()
    except KeyboardInterrupt:
        print('press ctrl + c to exit')


def invManagement():
    areaLoot(last["loot"])
    daJunk(last["da"])
    chompSharks(last["shark"])
    areaLoot(30)  # force an area loot before noting
    # it will likely do str first but can end up on others first cuz of delays
    notePotions(last["note"], './assets/NoteMe/superstrength.png')
    notePotions(last["note"], './assets/NoteMe/superdefence.png')
    notePotions(last["note"], './assets/NoteMe/superattack.png')


#
# Looks over all the files in the specified path to see if any are valid
# Args: the path ('./notepaper'), the confidence interval (.55), whether or not its grayscale (True),
# matchesrequired is how many matches in the dir it should have to find, returnFilesList is a boolean that changes the return from true to a list of matched images
# .55 and 2 are good for conf and matchesrequired for notepaper i think?
#


def checkItemExistence(path, conf, gray, matchesRequired, returnFilesList):
    image_list = []  # gets populated with strings of paths to the files. Function returns this if returnFilesList is True
    matches = 0  # matches pag found
    directory = os.listdir(path)  # get all the files in the directory
    for file in directory:  # for each file thats in the directory
        if file.endswith('.png') or file.endswith('.jpg'):  # if its a compatible image
            image_list.append(path + file)  # example: list[0]= "./assets/shark.png"
    for file in image_list:  # after it gets them all, for each one it found
        if pag.locateOnScreen(file, grayscale=gray, confidence=conf, region=REGION) is not None:  # if it can find it on screen
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
    if time.time() - lastshark > intervals["shark"] + rand.randrange(2, 5):
        # go until all the sharks are chompt, or you've gone thru 5 times cuz then somethings probably wrong
        while checkItemExistence('./assets/shark.png', .5, False, 1, False):
            print('press shark key')
            # keyboard.press(sharkKey)
            last["shark"] = time.time()
            count += 1
            if count > 4:
                break
            sleep(rand.randrange(0.6, 1.2, 1))  # hang out for a tick or two

# done


def areaLoot(lastloot):
    if time.time() - lastloot > intervals["loot"]:
        rs()
        # keyboard.press("space")
        print('pressed space to area loot')
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
        # keyboard.press(aggroKey)
        last["aggro"] = time.time()
        return True
    else:
        return False


# see if its been a while since we re-openeed the loot interface, then press the loot interface key if it has
def checkLootInterface(lastinterface):
    if time.time() - lastinterface > intervals["lootInterface"]:
        rs()
        print('opened loot interface')
        # keyboard.press(lootInterfaceKey)
        last["interface"] = time.time()
        return True
    else:
        return False


# dissassembles anything inside the da folder, repeats until its all gone
def daJunk(lastda):
    if time.time() - lastda > intervals["da"] and checkItemExistence('./assets/da/', .6, True, 1, False):
        daList = checkItemExistence('./assets/da/', .6, True, 1, True)
        print(daList)
        if checkItemExistence('./assets/da/', .6, True, 1, False):
            for itemToDa in daList:
                rs()
                print('press da key')
                # keyboard.press(daKey)
                pag.move(pag.locateOnScreen(itemToDa, grayscale=False, confidence=.65, region=REGION), duration=1)
                # pag.click()
                adjust(4, 6)
                print('clicked junk')
                last["da"] = time.time()


# returns true or false based on whether or not it noted pots
# pass last["note"] for a legit check, or pass a number bigger number to force it
# pass file as the path to the super pot image to check against
def notePotions(lastnote, file):
    if time.time() - lastnote > intervals["note"] + rand.randrange(1, 6):
        notepaperList = checkItemExistence('./assets/notepaper/', .58, True, 2, True)
        if len(notepaperList) >= 2:
            for i in pag.locateAllOnScreen(file, grayscale=False, confidence=0.8, region=REGION):
                pag.moveTo(notepaperList[0], duration=1)
                adjust(6, 10)
                # pag.click()
                print('click notepaper')
                pag.moveTo(i, duration=1)
                adjust(6, 10)
                print('click pot')
                # pag.click()  # add the check for "notepaper ->"
                last["note"] = time.time()
                return True
    return False


def rs():
    sleep(rand.randrange(2.0, 6.0, 1))


# x and y are the offsets on the respective axies
def adjust(x, y):
    x = rand.randrange(0, x)
    y = rand.randrange(0, y)
    pag.moveRel(x, y, 1)


if __name__ == '__main__':
    main()
