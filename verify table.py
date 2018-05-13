# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:17:33 2018

@author: Chaoyu
"""

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.w3schools.com/html/html_tables.asp')

def assert_table_text(table, row_num, col_num, expected_text):
    my_table=driver.find_element_by_id(table)
    all_rows=my_table.find_elements_by_tag_name('tr')
    my_row=all_rows[row_num]
    all_cols=my_row.find_elements_by_tag_name('td')
    my_col=all_cols[col_num-1]
    actual_text=my_col.text
    if expected_text not in actual_text:
        raise AssertionError('expected text %s not in row %s column %s,actual text is %s' % (expected_text,str(row_num),str(col_num), actual_text))
        
    
    
    else:
        print('pass. actual text is %s' % (actual_text))


assert_table_text('customers',1,1,'Alfreds')
