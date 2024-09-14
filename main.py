from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your WebDriver executable
chrome_driver_ip = '192.168.0.39'

# Setup Chrome options (optional)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode if you don't need a GUI

# Initialize the WebDriver
driver = (webdriver.Remote
    (command_executor=f'http://{chrome_driver_ip}:4444/wd/hub',
    options = chrome_options))

# Open a webpage
driver.get('http://www.youtube.com')

def find_element_by_xpath(xpath):
    return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))

# Accepting the cookies within 20 seconds
accepting_cookies = '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button'
find_element_by_xpath(accepting_cookies).click()
# Detecting and entering txt into searchbar
search_bar = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
find_element_by_xpath(accepting_cookies).send_keys("Programming")
# Searching and clicking on search button
search_icon = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button/yt-icon/span/div'
find_element_by_xpath(search_icon).click()

