from selenium import webdriver 
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)
    
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    
    button = browser.find_element_by_tag_name("button")
    button.click()
     
finally:
    time.sleep(30)
    browser.quit()   
    