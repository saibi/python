from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://item.gmarket.co.kr/Item?goodscode=3239486644")

price = driver.find_element(By.CLASS_NAME, "price_real")

print(price.text)

price = driver.find_element(
    By.CSS_SELECTOR, "SPAN.price_innerwrap-coupon strong.price_real")

print(price.text)

price = driver.find_element(
    By.XPATH, '//*[@id="itemcase_basic"]/div/div[3]/span[3]/strong')
print(price.text)

# driver.close() # one tab only
driver.quit()  # all tabs
