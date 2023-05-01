import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv('.env')

FB_EMAIL = os.getenv('ACCOUNT_EMAIL')
FB_PASSWORD = os.getenv('ACCOUNT_PASSWORD')
phone = os.getenv('PHONE_NUMBER')
chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')
url = os.getenv('TINDER_URL')

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

sleep(2)
login_button = driver.find_element(By.LINK_TEXT, 'Log in')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div[1]/div/div/div[3]'
                                         '/span/div[2]/button/div[2]/div[2]/div/div')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.TAB)
password.send_keys(Keys.ENTER)

time.sleep(5)
driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
phone_number = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div[1]/div/div[2]/div/input')
phone_number.send_keys(phone)
continue_button = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div[1]/div/button/div[2]/div[2]')
continue_button.click()
time.sleep(2)

notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]'
                                                    '/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.XPATH, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()
