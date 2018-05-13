# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:57:05 2018

@author: Chaoyu
"""

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://python.org/')

def element_exists(element_locator,element_text):
    try:
        driver.find_element(element_locator,element_text)
        return True
    except:
        return False
def assert_element_exists(element_locator, element_text):
    if not element_exists(element_locator, element_text):
        raise AssertionError("the element does not exist.")
    
    return

assert_element_exists('id','site-map-link')