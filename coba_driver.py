from selenium import webdriver
from threading import Thread

browser = webdriver.Firefox()
browser.get("http://dialogio.rf.gd/view/login.php")
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
#username = browser.find_element_by_id("username") #username form field
#Thread.sleep(10)
browser.quit()


print(innerHTML)
# password = browser.find_element_by_id("password_id") #password form field