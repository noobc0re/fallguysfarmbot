import pyautogui
import time

money=0
xp=0

print('plz minimize terminal')
time.sleep(3)

def inLobby():
    print('in lobby')
    pyautogui.press('space')

def inGame():
    print('in game')
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(0.5)
    pyautogui.press('space')

def inResults():
    print('disqualified')
    global money
    global xp
    money += 30
    xp += 15
    print('you have recieved '+str(money)+' money and '+str(xp)+'xp')
    time.sleep(5)
    pyautogui.press('space')

def inPopup():
    print('in popup')
    pyautogui.press('space')

while True:
    lobby=pyautogui.locateOnScreen('lobby.png')
    game=pyautogui.locateOnScreen('game.png')
    results=pyautogui.locateOnScreen('results.png')
    popup=pyautogui.locateOnScreen('popup.png')

    if lobby:
        inLobby()

    if game:
        inGame()
    
    if results:
        inResults()

    if popup:
        inPopup()