# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.parse import quote

import time

# # Config
login_time = 40                 # Time for login (in seconds)
new_msg_time = 10                # TTime for a new message (in seconds)
send_msg_time = 5               # Time for sending a message (in seconds)
country_code = 91               # Set your country code
action_time = 10                # Set time for button click action
image_path = 'image.png'        # Absolute path to you image

# # Create driver


# msg='For Sale, Purchase - Plot, Flat, floor, Villa And Shops in Wave City NH24. Best Deal Contact : 9999534995/6397263732'

# # Open browser with default link
# link = 'https://web.whatsapp.com'
# driver.get(link)
# time.sleep(login_time)

# # Loop Through Numbers List
# nums=['9999534995','7838133991','9582773798','8510051587','8506812838']


def send_messages(nums, msg):
   service = Service()
   options = webdriver.ChromeOptions()
   driver = webdriver.Chrome(service=service, options=options)
   driver.maximize_window()
   link = 'https://web.whatsapp.com'
   driver.get(link)
   time.sleep(login_time)
   for num in nums:
    print('Message In loop', msg)
    encoded_msg=quote(msg)
    link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={encoded_msg}'
    print('Link in loop', link)
    driver.get(link)
    time.sleep(new_msg_time)
    action=ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(send_msg_time)
   # Quit the driver
   driver.quit()
