from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.CSS_SELECTOR, "div#articlecount a:first-child")
print(count.text)
# count.click()

# view_history = driver.find_element(By.LINK_TEXT, "View history")
# view_history.click()


search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()
