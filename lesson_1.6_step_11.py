from selenium import webdriver
import time 

link1 = "http://suninjuly.github.io/registration1.html"   #тест 1

try:
    browser = webdriver.Chrome()
    browser.get(link1)

    input1 = browser.find_element_by_css_selector(".first_block .first_class > input")
    input1.send_keys("Lyudmila")
    input2 = browser.find_element_by_css_selector(".first_block .second_class > input")
    input2.send_keys("Glazacheva")
    input3 = browser.find_element_by_class_name("form-control.third")
    input3.send_keys("l.glazacheva2014@yandex.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()  
    
link2 = "http://suninjuly.github.io/registration2.html"  #тест 2

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    input1 = browser.find_element_by_css_selector(".first_block .first_class > input")
    input1.send_keys("Lyudmila")
    input2 = browser.find_element_by_css_selector(".first_block .second_class > input")
    input2.send_keys("Glazacheva")
    input3 = browser.find_element_by_class_name("form-control.third")
    input3.send_keys("l.glazacheva2014@yandex.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()  
    