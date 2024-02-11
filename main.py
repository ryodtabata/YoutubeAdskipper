import pyautogui
from time import sleep

pyautogui.FAILSAFE = True
path = "skipbutton.png"


while True:
    sleep(0.45)
    try:
        button_coordinates = pyautogui.locateCenterOnScreen(path, confidence=0.97) or pyautogui.locateCenterOnScreen(path2, confidence=0.8) or pyautogui.locateCenterOnScreen(path3, confidence=0.8) or pyautogui.locateCenterOnScreen(path4, confidence=0.8)
        print(button_coordinates)
        if button_coordinates is not None:
            pyautogui.click(1380,788)
    except pyautogui.ImageNotFoundException:
        print("None")
    sleep(1)

