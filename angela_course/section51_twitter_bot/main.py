import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

PROMISED_DOWN = 100
PROMISED_UP = 100
TWITTER_EMAIL = ""
TWITTER_USERNAME = ""
TWITTER_PASSWORD = ""


class SpeedTwitt:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def check_speed(self):
        self.driver.get("https://www.speedtest.net/")
        print("sleep 5")
        time.sleep(5)

        privacy_popup_button = self.driver.find_element(
            By.ID, "onetrust-accept-btn-handler")
        privacy_popup_button.click()

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        print(go_button.text)
        go_button.click()

        print("sleep 60")
        time.sleep(60)

        download_speed = self.driver.find_element(
            By.CLASS_NAME, "download-speed")
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")

        self.download_speed = download_speed.text
        self.upload_speed = upload_speed.text

    def tweet(self):
        self.driver.get("https://twitter.com/")
        print("sleep 5")
        time.sleep(5)

        login_button = self.driver.find_element(By.LINK_TEXT, "Sign in")
        login_button.click()

        print("sleep 3")
        time.sleep(3)

        username_input = self.driver.find_element(By.TAG_NAME, "input")
        username_input.send_keys(TWITTER_EMAIL)
        username_input.send_keys(Keys.ENTER)

        print("sleep 3")
        time.sleep(3)

        try:
            pass_input = self.driver.find_element(
                By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)

        except NoSuchElementException:
            username = self.driver.find_element(
                By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            # Your Username here in case Twitter asks for username before asking password
            username.send_keys(TWITTER_USERNAME)
            username.send_keys(Keys.ENTER)
            time.sleep(5)
            pass_input = self.driver.find_element(
                By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)

        print("twitter login success")
        print("sleep 5")
        time.sleep(5)

    def quit(self):
        self.driver.quit()


test = SpeedTwitt()
test.check_speed()
print(f"download speed : {test.download_speed}")
print(f"upload speed : {test.upload_speed}")
test.tweet()
test.quit()
