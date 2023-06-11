import os
from undetected_chromedriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup

url = 'https://double.turbogames.io/'

# Configure Chrome driver options
chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

# Set Chrome driver path
chrome_driver_path = os.environ.get("CHROMEDRIVER_PATH")

# Initialize the WebDriver
driver = Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get(url)

page_source = driver.page_source

print(page_source)

driver.quit()
