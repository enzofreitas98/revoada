import undetected_chromedriver as uc
from selenium import webdriver
import os

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = uc.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
driver.get("https://double.turbogames.io/")
print(driver.page_source)
