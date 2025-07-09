# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 18:50:50 2025
File name:  

@author:    Ahmed El-Abbasy
@contact:   https://www.linkedin.com/in/ahmed-el-abbasy-938827187/
"""

from Pages_locators.Locators import Loc_Inf 
import time 
import pytest 

pytestmark = pytest.mark.order(1)

# Open Chrome with Selenuim
@pytest.mark.order(1)
def test_login():
    action_1 = {
        "url"               :     "https://www.linkedin.com/",
    }
    page = Loc_Inf(action_1)
    page.execute()