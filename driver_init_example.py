from selenium import webdriver
from selenium.webdriver.chrome.service import Service
CHROME_DRIVER_PATH = r"C:\Program Files (x86)\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)

# Initialize Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=service,options=chrome_options) 

driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()