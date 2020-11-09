import pytest
import requests
import time
from selenium import webdriver

def test_wikipedia():
    driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
    driver.get('https://en.wikipedia.org/');
    time.sleep(5) # Let the user actually see something!
    search_box = driver.find_element_by_name('search')
    search_box.send_keys('wake tech')
    search_box.submit()
    time.sleep(5) # Let the user actually see something!
    title = driver.find_element_by_id('firstHeading')
    assert (title.text == "Wake Technical Community College")
    driver.quit()





        
    
    