from selenium import webdriver
import time
import os
current_dir = os.getcwd()  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'dataset.txt')   # добавляем к этому пути имя файла

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Lyudmila")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Glazacheva")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("nit")
    
    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)
    
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    
finally:
    time.sleep(30)
    browser.quit()
    