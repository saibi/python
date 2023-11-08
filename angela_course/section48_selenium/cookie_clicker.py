from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
btn = driver.find_element(By.ID, "cookie")
btn.click()


def get_available_items():
    items = driver.find_elements(
        By.CSS_SELECTOR, "#store div[id^=buy]:not(.grayed)")
    items.reverse()
    return items


loop_end = time.time() + 10 * 60
check_interval = 3
timeout = time.time() + check_interval * 1
while time.time() < loop_end:
    btn.click()

    if time.time() > timeout:
        items = get_available_items()
        if len(items) > 1:
            print(f"click {items[0].text}")
            items[0].click()

        check_interval += 1
        timeout = time.time() + check_interval * 1

print("end")

# driver.quit()
