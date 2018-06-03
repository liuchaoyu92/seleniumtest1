# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')
dropdown=driver.find_element_by_xpath('//*[@id="searchDropdownBox"]')
def select_dropdown_option_by_text(my_dropdownmenu, expected_text):
    all_options=my_dropdownmenu.find_elements_by_tag_name('option')
    option_found=False
    for option in all_options:
        if option.text==expected_text:
            option.click()
            option_found=True
            break
    if not option_found:
        raise AssertionError('No such option as %s' % expected_text)
    return
select_dropdown_option_by_text(dropdown,'Books')