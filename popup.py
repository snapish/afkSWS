from operator import contains
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

sharkKey = ""
lootInterfaceKey = ""
aggroPotKey = ""
daKey = ""
daBool = False


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    textLabel = QLabel(widget)
    grid = QGridLayout()
    widget.setLayout(grid)

    sharkBox = QLineEdit()
    lootInterfaceBox = QLineEdit()
    aggroBox = QLineEdit()
    daBox = QLineEdit()

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

    widget.setGeometry(1200, 500, 500, 500)
    widget.setWindowTitle("Bot Config")
    checkbox = QCheckBox(widget)
    checkbox.setText("Disassemble Warpriest and junk")
    grid.addWidget(sharkBox)
    grid.addWidget(lootInterfaceBox)
    grid.addWidget(daBox)
    grid.addWidget(aggroBox)
    grid.addWidget(checkbox)
    grid.addWidget(textLabel)
    checkbox.clicked.connect(toggleDa)

    lootInterfaceBox.show()
    daBox.show()
    aggroBox.show()
    sharkBox.show()
    widget.show()
    checkbox.show()
    sys.exit(app.exec_())


def main():
    pass


def takeInputs():
    print(daBool)


def toggleDa():
    global daBool
    daBool ^= True
    print(daBool)


if __name__ == '__main__':
    window()
