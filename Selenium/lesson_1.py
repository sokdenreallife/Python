from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com")
print(driver.title)

time.sleep(30) # Time delay
driver.quit() # Close browser
driver.close() # Close tab browser
