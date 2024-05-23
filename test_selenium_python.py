# Ensure your script is not named selenium.py

# Import required classes from selenium
import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Ensure chromedriver.exe is in the correct path or provide the full path
service = Service("C:/Users/User/OneDrive/Рабочий стол/selenium/chromedriver.exe")

# Create an instance of ChromeOptions
options = webdriver.ChromeOptions()

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the specified URL
driver.get("https://userinyerface.com/game.html")
time.sleep(15)

# Add additional code here if you need to interact with the page

# Close the driver
driver.quit()
