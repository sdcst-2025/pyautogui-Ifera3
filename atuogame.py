#!Python 3

import time
import pyautogui as gui
gui.FAILSAFE = True

def start():
    #time.sleep(10)
    #print(locatoin)
    locatoin = gui.locateCenterOnScreen('images/Chrome.png')
    gui.leftClick(locatoin.x, locatoin.y)
    #time.sleep(5)
    locatoin = gui.locateCenterOnScreen('images/reload.png')
    gui.leftClick(locatoin.x, locatoin.y)
    time.sleep(1)
    locatoin = gui.locateCenterOnScreen('images/playbutton.png',confidence=0.9)
    gui.leftClick(locatoin.x, locatoin.y)
    time.sleep(3.5)
    locatoin = gui.locateCenterOnScreen('images/Screenshot 2025-05-20 105908.png',confidence=0.8)
    gui.leftClick(locatoin.x, locatoin.y)

def mainloop():
    while gui.FAILSAFE == True:
        print(1)
        gui.failSafeCheck()

start()
mainloop()