from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3751679953&keywords=python%20developer&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true")

signin = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
print("sleep 5")
time.sleep(5)
print(signin.text)
signin.click()

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

print("enter username and password")
username.send_keys("username")
password.send_keys("password")

signin = driver.find_element(
    By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
signin.click()
print("sleep 5")
time.sleep(5)

all_jobs = driver.find_elements(
    By.CSS_SELECTOR, '.jobs-search-results__list-item')
for listing in all_jobs:
    page = listing.find_element(By.CSS_SELECTOR, '.job-card-list__title')
    print("Job Title: " + page.text)

# driver.close() # one tab only
# driver.quit()  # all tabs
