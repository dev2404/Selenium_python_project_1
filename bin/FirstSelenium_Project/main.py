import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(5)

#Open page
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(10)

#Type username student into Username field
username_loc = driver.find_element(By.ID, "username")
username_loc.send_keys("student")

#Type password Password123 into Password field
password_loc = driver.find_element(By.NAME, "password")
password_loc.send_keys("Password123")

#Puch Submit button
submit_button_loc = driver.find_element(By.XPATH, "//Button[@class='btn']")
submit_button_loc.click()

#Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

#Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_loc = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_loc.text
assert actual_text == "Logged In Successfully"

#Verify button Log out is displayed on the new page
logout_button_loc = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_button_loc.is_displayed()

