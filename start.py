# 10 PRAYER BONUS CALCULATIONS: aers gives 370 points, a prayer renewal gives 454 every 5 mins. Puts us at like -254 prayer points per minute, so 3/5 minutes we can SS
#assume 100 paper/hr
import time
from time import sleep
import random as rand
import pyautogui as pag
import os
import concurrent.futures
import keyboard

REGION = (960, 540, 1920, 1080)
# get input for a password that md5s against something probably
intervalMinimumSeconds = {"da": 10,"aggro": 290, "shark": 45,"loot": 45, "lootInterface": 300, "aers": 300, "ss": 30}
sharkKey = "v"
lootInterfaceKey = "m"
daKey = "8"
lastShark = 0
lastLoot = 0


def main():
    invManagement()
    

def invManagement():
    attackLocations = pag.locateOnScreen('superattack.png', grayscale=True, confidence=0.7, region=REGION)
    notepaperLocations = pag.locateOnScreen('./assets/notepaper/', grayscale=True, confidence=0.7, region=REGION)

    for i in pag.locateAllOnScreen('./assets/superattack.png', grayscale=False, confidence=0.8, region=REGION):
        if checkItemExistence('./assets/notepaper/', .58, True, 2):
            pag.moveTo(notepaperLocations, duration=1)
            x = rand.randrange(0, 6)
            y = rand.randrange(0, 10)
            pag.moveRel(x, y, 1)
            pag.click()
            pag.moveTo(i, duration=1)
            x = rand.randrange(0, 6)
            y = rand.randrange(0, 10)
            pag.moveRel(x, y, 1)
            pag.click()
        break

#
# Looks over all the files in the specified path to see if any are valid
# Args: the path ('./notepaper'), the confidence interval (.55), whether or not its grayscale (True), 
# matchesrequired is how many matches in the dir it should have to find, returnFilesList is a boolean that changes the return from true to a list of matched images
# .55 and 2 are good for conf and matchesrequired for notepaper i think?
#
def checkItemExistence(path, conf, gray, matchesRequired, returnFilesList):
    image_list = []
    matches = 0
    directory = os.listdir(path)  # './notepaper'
    for file in directory:
        if file.endswith('.png') or file.endswith('.jpg'):
            image_list.append(path + file)

    for file in image_list:
        if pag.locateOnScreen(file, grayscale=gray, confidence=conf, region=REGION) is not None:
            matches += 1

    if matches >= matchesRequired and not returnFilesList:
        return True
    elif not returnFilesList:
        return False
    else:
        return image_list
# remember to do after cuz pots are worth more


def chompSharks(lastshark):
    count = 0
    if time.time() - lastshark > intervalMinimumSeconds["shark"] + rand.randrange(2,5):
        # go until all the sharks are chompt, or you've gone thru 5 times cuz then somethings probably wrong
        while checkItemExistence('./assets/shark.png', .5, False, 1, False):
            keyboard.press(sharkKey)
            lastShark = time.time()
            count += 1
            if count > 4:
                break
            sleep(rand.randrange(0.6, 1.2, .1))  # hang out for a tick or two


def areaLoot(lastloot):
    if time.time() - lastloot > intervalMinimumSeconds["loot"]:
        rs()
        keyboard.press("space")
        return True
    else: return False

def upkeepOverload(lastovl):
    if time.time() - lastovl > intervalMinimumSeconds["aggro"] :
        rs()
        keyboard.press('c')
        return True
    else: return False

def checkLootInterface(lastinterface):
    if time.time() - lastinterface > intervalMinimumSeconds["lootInterface"]:
        rs()
        keyboard.press(lootInterfaceKey)
        return True
    else: return False

def daJunk(lastda):
    daList = checkItemExistence('./assets/da/', .6, True, 1, True)
    if checkItemExistence('./assets/da/', .6, True, 1, False) and time.time() - lastda > intervalMinimumSeconds["da"]:
        rs()
        print('press da key')
        #keyboard.press(daKey)
        pag.move(pag.locateOnScreen(daList[0], grayscale=True, confidence=.6, region=REGION), duration= 1)
        print('click da junk')


        




def rs():
    sleep(rand.randrange(2.0,6.0, .314249))

if __name__ == '__main__':
    main()
