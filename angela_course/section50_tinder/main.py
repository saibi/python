from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")
time.sleep(3)

login = driver.find_element(By.LINK_TEXT, "Log in")
# login = driver.find_element( By.XPATH, '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
print(login.text)
login.click()
time.sleep(2)
google_login = driver.find_element(
    By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[1]/div/div/div/iframe')
google_login.click()
time.sleep(5)

base_window = driver.window_handles[0]
popup_window = driver.window_handles[1]

driver.switch_to.window(popup_window)
print(driver.title)


# driver.close() # one tab only
# driver.quit()  # all tabs
