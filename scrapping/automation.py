from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

assert "Selenium Easy Demo" in chrome_browser.title
show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
assert "Show Message" in show_message_button.get_attribute("innerHTML") 
user_message = chrome_browser.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys("SELENIUM IS EXTRA COOL") 

show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
show_message_button.click()

output_message = chrome_browser.find_element(By.ID, "display")
assert "SELENIUM IS EXTRA COOL" in output_message.text

chrome_browser.quit()

