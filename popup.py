from dataclasses import dataclass
from operator import contains
from tkinter import Toplevel
import pyautogui as pag
import sys
import random as rand
import keyboard
import cv2
import os
import concurrent.futures
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from time import sleep

REGION = (960, 540, 1920, 1080)

assignments = {"daKey": "", "sharkKey": "", "aggroKey": "", "lootInterfaceKey": "", "daBool": False}
validated = False
topLeft = ()
bottomRight = ()


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    grid = QGridLayout()
    widget.setLayout(grid)
    sharkLabel = QLabel()
    sharkBox = QLineEdit()
    lootInterfaceLabel = QLabel()
    lootInterfaceBox = QLineEdit()
    aggroLabel = QLabel()
    aggroBox = QLineEdit()
    daLabel = QLabel()
    daBox = QLineEdit()
    failedToValidateLabel = QLabel()
    continueButton = QPushButton()

    widget.setGeometry(1200, 500, 500, 500)
    widget.setWindowTitle("Bot Config")

    sharkLabel.setText("Eat Shark key")
    lootInterfaceLabel.setText("Open Loot Interface key")
    aggroLabel.setText("Aggro pot / aggroverload key")
    daLabel.setText("Dissassemble Button")
    failedToValidateLabel.setText("Please fill out all the text boxes")

    continueButton.setText("Continue")
    continueButton.clicked.connect(submit)

    aggroBox.setMaxLength(1)
    aggroBox.setMaximumWidth(100)
    aggroBox.setPlaceholderText("Aggro pot key")

    sharkBox.setMaxLength(1)
    sharkBox.setMaximumWidth(100)
    sharkBox.setPlaceholderText("Eat shark key")

    lootInterfaceBox.setMaxLength(1)
    lootInterfaceBox.setMaximumWidth(100)
    lootInterfaceBox.setPlaceholderText("Open area loot key")

    daBox.setMaxLength(1)
    daBox.setMaximumWidth(100)
    daBox.setPlaceholderText("DA Key")

    checkbox = QCheckBox(widget)
    checkbox.setText("Disassemble Warpriest and junk")
    checkbox.clicked.connect(toggleDa)
    # grid.addWidget(failedToValidateLabel)

    grid.addWidget(sharkBox, 0, 0,)
    grid.addWidget(sharkLabel, 0, 1)
    grid.addWidget(daBox, 1, 0)
    grid.addWidget(daLabel, 1, 1)
    grid.addWidget(aggroBox, 2, 0)
    grid.addWidget(aggroLabel, 2, 1)
    grid.addWidget(lootInterfaceBox, 3, 0)
    grid.addWidget(lootInterfaceLabel, 3, 1)

    grid.addWidget(checkbox)
    grid.addWidget(continueButton)

    aggroBox.show()
    sharkBox.show()
    lootInterfaceBox.show()
    daBox.show()
    continueButton.show()
    widget.show()

    if validateAssignments():
        writeKeysToFile()
        validated = True
    #     widget.close()
    sys.exit(app.exec_())


def writeKeysToFile():
    pass

# makes sure they got all the text boxes


def validateAssignments():
    flag = False
    if assignments["sharkKey"] != "" and assignments["aggroPotKey"] != "" and assignments["lootInterfaceKey"] != "" and not assignments["daBool"]:  # if all the fields are filled in, only including the dissassemble key if they want to da things
        if assignments["daBool"] and assignments["daKey"] != "":  # go to this line only if the keys have assignments.
            flag = True  # mark everythign as good to go if they checked the dissassemble box, and the disassemble key is assigned
        elif not assignments["daBool"]:  # if the checkbox isnt checked
            flag = True  # were still good
    return flag

# for the checkbox of whether or not they want to disassemble things


def toggleDa():
    assignments["daBool"] ^= True
    print(assignments["daBool"])


def main():
    pass

# monitor mosue and get the specified region from the user.
# for inv reginon


def drawBox():
    global topLeft
    global bottomRight

# the done button on the dialog box


def submit():

    pass


if __name__ == '__main__':
    window()
