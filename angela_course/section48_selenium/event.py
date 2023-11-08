from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

li_list = driver.find_elements(By.CSS_SELECTOR, "div.event-widget ul.menu li")

event_list = {}
event_index = 0
print(len(li_list))
for tag in li_list:
    date_text = tag.find_element(By.TAG_NAME, "time").text
    event_text = tag.find_element(By.TAG_NAME, "a").text
    event_list[event_index] = {"time": date_text, "name": event_text}
    event_index += 1

driver.quit()

print(event_list)
