from PIL  import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *
 
class coords():
    replayButton = (960, 510)
    Dinosaur=(668,452)
 
def replay():
    pyautogui.click(coords.replayButton)
 
def jump():
    pyautogui.keyDown('space')
    time.sleep(0.01 )
    pyautogui.keyUp('space')
 
 
def pixelSum():
    box = (224, 561, 556, 662)
    image=ImageGrab.grab(box
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    return(a.sum())
 
def main():
 
    val=pixelSum()
    if val!=33779:
 
        print(val,'Jump')
        jump()
 
time.sleep(5)
replay()
while True:
    main()
