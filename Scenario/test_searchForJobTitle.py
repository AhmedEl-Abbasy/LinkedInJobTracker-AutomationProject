# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 19:10:50 2025
File name:  

@author:    Ahmed El-Abbasy
@contact:   https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""
import pyautogui
import pytest 

pytestmark = pytest.mark.order(2)

@pytest.mark.order(1)
def test_searchForJob():
    print("searchForJob")

    # time.sleep(30)
    pointForimg = pyautogui.locateOnScreen("imgesForScripts/jobIcon.png" , confidence=0.8)
    pyautogui.moveTo(pyautogui.center(pointForimg))

    pyautogui.click(pyautogui.center(pointForimg))    
    
    pyautogui.sleep(5)
    pointForimg = pyautogui.locateOnScreen("imgesForScripts/locationIcon.png" , confidence=0.8)
    pyautogui.click(pyautogui.center(pointForimg))
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write("Egypt")

    pyautogui.sleep(0.5)
    pointForimg = pyautogui.locateOnScreen("imgesForScripts/searchIcon.png" , confidence=0.8)
    pyautogui.click(pyautogui.center(pointForimg))
    pyautogui.write("Test Automation")
    pyautogui.sleep(1)
    pyautogui.press('enter')


    pyautogui.sleep(5)
    pyautogui.screenshot("Output/JobResult.png")

