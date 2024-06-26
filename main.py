import pyautogui as pag
import random
import time

while True:
    #Edit the x and y upper and lower bounds as per your monitor size
    #Tip: Do not make them too wide
    x = random.randint(600, 1000)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)

    #press the shift key to prevent a screensaver. You may need to change the key depending on which program is open while your are afk
    pag.press('shift')

    #left clicks
    pag.click()

    time.sleep(2) #Do not set this value too low