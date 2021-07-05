# This is notes not a project

from selenium import webdriver
# import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time
from bs4 import BeautifulSoup as bs

# Using this chrome option to get desired UI like testing in the terminal or removing the selenium 
# notification.
CHROME_OPTIONS = ChromeOptions()
# CHROME_OPTIONS.add_experimental_option('excludeSwitches', ['enable-automation'])

BASE_DIR = os.path.dirname('__file__')
# DRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver.exe')
DRIVER_PATH = 'C:/Users/Brothers/SMIT-PROJRC/PROJ.RC/__operational files__/github repo/Artificial Intelligence/GUI_Automation/Google Search Automation using Selenium/chromedriver.exe'
# Reffering to web driver executable file.
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=CHROME_OPTIONS)

# Requesting the webpage
driver.get('https://emojitracker.com/')
# Finding the search bar to send the key strokes.
# search_bar = driver.find_element_by_xpath(
#                     '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
input('Press enter')
page_source = driver.page_source
# print(page_source)
soup = bs(page_source)
print(soup)
with open("output.html", "w", encoding='utf-8') as file:
    file.write(str(soup))

# Start an new tab
# driver.execute_script("window.open('https://www.facebook.com/groups/2395385783831009','_blank');")
# [1] means new_tab 1
# driver.switch_to.window(driver.window_handles[1])
# For Fullscreen
# driver.fullscreen_window()

# def search():
#     query = input("Google: Please give your query\n\nYou: ")
#     # This method is used to send the key stroke to the browser.
#     search_bar.send_keys(query)
#     search_bar.send_keys(Keys.CONTROL, 't')
#     # Pressing Enter key
#     search_bar.send_keys(Keys.ENTER)

# search()
if not(input("Press enter to exit")):
    # time.sleep(60)
    # driver.close will only close the tab at index 0
    # https://www.edureka.co/community/52772/close-active-current-without-closing-browser-selenium-python
    driver.close()