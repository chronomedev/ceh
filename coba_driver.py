from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://dialogio.rf.gd/view/login.php")
time.sleep(10)
driver.quit()

username = browser.find_element_by_id("userid") #username form field
print(username)
# password = browser.find_element_by_id("password_id") #password form field