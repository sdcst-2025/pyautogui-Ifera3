#!Python 3

#https://quanran.itch.io/slimeow-game

import time
import pyautogui as gui
gui.FAILSAFE = True

notYet = 'images/unavalible.png'#'images/zero.png'
notYet100 = 'images/unwork100.png'
buttonList = []

class button():
    def __init__(self,buttonImage):
        #print(buttonImage)
        self.clicks = 0
        self.image = buttonImage
        locationSize = gui.locateOnScreen(self.image,confidence=0.9)
        self.x = locationSize.left - 20
        self.y = locationSize.top - 20
        self.height = locationSize.height + 50
        self.width = locationSize.width + 150
        print(self.x,self.y,self.x+self.width,self.y+self.height)
        #gui.moveTo(self.x+self.width,self.y+self.height)
    
    def isAvalible(self):
        try:
            gui.locateOnScreen(notYet,region=(self.x,self.y,self.x+self.width,self.y+self.height))
            #print('pass 1',self.image)
            return False
        except: 
            try:
                gui.locateOnScreen(notYet100,region=(self.x,self.y,self.x+self.width,self.y+self.height))
                #raise
                #print('pass 2',self.image)
                return False
            except:
                return self.activate()

    def activate(self):
        self.clicks += 1
        #print(self.clicks)
        time.sleep(1)
        gui.moveTo(self.x+(0.5*self.width), self.y+(0.5*self.height))
        gui.leftClick(self.x+(0.5*self.width), self.y+(0.5*self.height))
        return True

class buttonbreed(button):
    def __init__(self, buttonImage):
        super().__init__(buttonImage)
    
    def isAvalible(self):
        global buttonList
        if super().isAvalible():
            time.sleep(1)
            if self.clicks == 3:
                location = gui.locateOnScreen("images/towr.png",confidence=0.9)
                plus = gui.locateOnScreen("images/plus.png",region=(location.left,location.top-100,location.left+location.width,location.top+location.height),confidence=0.9)
            else:
                location = gui.locateOnScreen("images/pond.png",confidence=0.9)
                plus = gui.locateOnScreen("images/plus.png",region=(location.left,location.top-140,location.left+location.width,location.top+location.height),confidence=0.98)
            #print(location)
            gui.moveTo(plus.left+(0.5*plus.width),plus.top+(0.5*plus.height))
            gui.leftClick(plus.left+(0.5*plus.width),plus.top+(0.5*plus.height))
            if self.clicks == 2:
                buttonList.insert(0,button('images/moreFish.png'))
            elif self.clicks == 3:
                buttonList.append(button('images/biggerBowl.png'))
                buttonList.append(button('images/Veteran.png'))
            elif self.clicks == 4:
                buttonList.append(button('images/quickMeow.png'))
            elif self.clicks == 5:
                buttonList.insert(1,button('images/fishyResearch.png'))

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
    start()
    time.sleep(0.5)
    buttonList.append(buttonbreed("images/breedSlimeow.png"))
    while gui.FAILSAFE == True:
        for button in buttonList:
            button.isAvalible()
            gui.failSafeCheck()
        #print(1)
    #button = gui.locateOnScreen("images/breedSlimeow.png",confidence=0.9)
    #print(button)
    #gui.moveTo(button.left, button.top)
    #time.sleep(0.5)
    #gui.moveTo(button.left + button.width+65, button.top + button.height)

if __name__ == "__main__":
    mainloop()