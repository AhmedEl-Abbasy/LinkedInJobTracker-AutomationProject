# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 21:17:13 2025
File name:  

@author:    Ahmed El-Abbasy
@contact:   https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""
import pyautogui
import pytest 
import os

pytestmark = pytest.mark.order(3)

def test_send2whatsapp():
    screenshot_path = "./Output/JobResult.png"
    os.system(f"xclip -selection clipboard -t image/png -i {screenshot_path}")
    
    pyautogui.sleep(1)
    pointForimg1 = pyautogui.locateOnScreen("imgesForScripts/imgForNewPage.png")
    pyautogui.click(pyautogui.center(pointForimg1))

    pyautogui.sleep(1)
    pyautogui.write(r"https://web.whatsapp.com/")
    pyautogui.press('enter')

    flag_time = 0
    while True:
        try:
            pointForimg1 = pyautogui.locateOnScreen("imgesForScripts/youChat.png", confidence=0.8)
            pyautogui.click(pyautogui.center(pointForimg1))
            break
        except:
            pyautogui.sleep(1)
            flag_time +=1
            if flag_time > 30:
                flag_time =0
                break

    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v') 
    

    flag_time = 0
    while True:
        try:
            pointForimg = pyautogui.locateOnScreen("imgesForScripts/sendIcon.png", confidence=0.8)
            pyautogui.sleep(1)
            pyautogui.click(pyautogui.center(pointForimg))
            break
        except:
            pyautogui.sleep(1)
            flag_time +=1
            if flag_time > 30:
                flag_time =0
                break

    pyautogui.press('enter')
    pyautogui.sleep(3)
    



