import os
import json
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv("env.env")
PROMISED_WON_MBPS = 100
PROMISED_UP_MBPS = 10
TWITTER_USERNAME = os.environ.get("T_USERNAME")
TWITTER_PASS = os.environ.get("PASS")


class InternetSpeedTwitterBot:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        self.driver = webdriver.Chrome(options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.set_window_position(500, 0)
        self.wait = WebDriverWait(self.driver, 100)
        self.down_result = None
        self.up_result = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        start_button = self.driver.find_element(By.CSS_SELECTOR, "span.start-text")
        start_button.click()

        back_to_test_results_locator = (By.LINK_TEXT, "Back to test results")
        self.wait.until(
            ec.presence_of_element_located(back_to_test_results_locator)
        )
        self.driver.find_element(By.LINK_TEXT, "Back to test results").click()

        down_result_element_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/'\
                                    'div/div[2]/div[1]/div[1]/div/div[2]/span'
        up_result_element_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/' \
                                  'div/div[2]/div[1]/div[2]/div/div[2]/span'
        self.down_result = self.driver.find_element(By.XPATH, down_result_element_xpath).text
        self.up_result = self.driver.find_element(By.XPATH, up_result_element_xpath).text


    def tweet_at_isp(self):
        twitter_cookies_file = open("twittercookies.txt")
        twitter_cookies: list = twitter_cookies_file.readlines()
        self.driver.get("https://twitter.com")

        print("Adding cookies...")
        for cookie in twitter_cookies:
            self.driver.add_cookie(json.loads(cookie))
        twitter_cookies_file.close()
        time.sleep(1)

        username_input = self.driver.find_element(By.TAG_NAME, "input")
        next_button_element = self.driver.find_element(By.XPATH, '//*[text()="Next"]')
        username_input.send_keys(TWITTER_USERNAME)
        next_button_element.click()
        time.sleep(1)

        pw_form = self.driver.find_element(By.NAME, "password")
        pw_form.send_keys(TWITTER_PASS, Keys.ENTER)




bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
# print(bot.down_result, bot.up_result)
# bot.driver.quit()
bot.tweet_at_isp()
input("Hit ENTER to get cookies.")
with open("twittercookies.txt", "w") as file:
    cookies = bot.driver.get_cookies()
    for cookie in cookies:
        cookie_string = json.dumps(cookie)
        file.write(f"{cookie_string}\n")
input("Cookies acquired. Hit ENTER to continue.")
bot.driver.quit()