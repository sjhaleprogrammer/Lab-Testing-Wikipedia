import pytest
import requests
import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://en.wikipedia.org/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('search')
search_box.send_keys('wake tech')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()




def test_wikipedia():
    print("test")




        
    
    