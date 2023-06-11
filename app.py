import undetected_chromedriver as uc 
# ... 
options = uc.ChromeOptions() 
 
options.headless = True 
 
driver = uc.Chrome(options=options) 
# ...
 
driver.get("https://double.turbogames.io/") 
 
print(driver.page_source)

