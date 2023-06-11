import undetected_chromedriver as uc
driver = uc.Chrome()
driver.get("https://double.turbogames.io/")
print(driver.page_source)
