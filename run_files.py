# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 17:11:20 2025
File name:  

@author:    Ahmed El-Abbasy
@contact:   https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""

# import sys, os
import pytest

if __name__ == "__main__":
    
    print("Hello")
    pytest_args = ['-rA', "-v" , "-s"]#  , "./Scenario/test_navigatewithPyautogui.py::test_send2whatsapp"]
    
    pytest.main(pytest_args)
    