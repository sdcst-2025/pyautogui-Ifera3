#!Python 3

import time
import pyautogui as gui
gui.FAILSAFE = True

notYet = 'images/unavalible.png'
buttonList = []

class button():
    def __init__(self,buttonImage):
        self.image = buttonImage
        locationSize = gui.locateOnScreen(self.image,confidence=0.9)
        self.x = locationSize.left
        self.y = locationSize.top
        self.height = locationSize.height
        self.width = locationSize.width + 65
        #gui.moveTo(self.x+self.width,self.y+self.height)
    
    def isAvalible(self):
        try:
            gui.locateOnScreen(notYet,region=(self.x,self.y,self.x+self.width,self.y+self.height))
            return False
        except:
            time.sleep(0.5)
            gui.leftClick(self.x+(0.5*self.width), self.y+(0.5*self.height))
            return True

class buttonbreed(button):
    def __init__(self, buttonImage):
        super().__init__(buttonImage)
    
    def isAvalible(self):
        if super().isAvalible():
            time.sleep(0.5)
            location = gui.locateOnScreen("images/pond.png",confidence=0.9)
            plus = gui.locateOnScreen("images/plus.png",region=(location.left,location.top,location.width+location.width,location.top+location.height),confidence=0.9)
            gui.moveTo(plus.left+(0.5*plus.width),plus.top+(0.5*plus.height))
            gui.leftClick(plus.left+(0.5*plus.width),plus.top+(0.5*plus.height))

def start():
    #time.sleep(10)
    #print(locatoin)
    locatoin = gui.locateCenterOnScreen('images/Chrome.png',confidence=0.9)
    gui.leftClick(locatoin.x, locatoin.y)
    #time.sleep(5)
    locatoin = gui.locateCenterOnScreen('images/reload.png')
    gui.leftClick(locatoin.x, locatoin.y)
    time.sleep(1)
    locatoin = gui.locateCenterOnScreen('images/playbutton.png',confidence=0.9)
    gui.leftClick(locatoin.x, locatoin.y)
    time.sleep(3.5)
    locatoin = gui.locateCenterOnScreen('images/start.png',confidence=0.8)
    gui.leftClick(locatoin.x, locatoin.y)

def mainloop():
    time.sleep(0.5)
    buttonList.append(buttonbreed("images/breedSlimeow.png"))
    #button = gui.locateOnScreen("images/breedSlimeow.png",confidence=0.9)
    #print(button)
    #gui.moveTo(button.left, button.top)
    #time.sleep(0.5)
    #gui.moveTo(button.left + button.width+65, button.top + button.height)
    while gui.FAILSAFE == True:
        buttonList[0].isAvalible()
        #print(1)
        gui.failSafeCheck()

start()
mainloop()