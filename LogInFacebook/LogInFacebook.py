from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time,os

load_dotenv()

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)

email =  driver.find_element(by=By.ID,value="email")
password = driver.find_element(by= By.ID,value="pass")
LogIn = driver.find_element(by=By.NAME,value="login")


email.send_keys(os.getenv("EMAIL"))
password.send_keys(os.getenv("PASS"))

LogIn.click()

time.sleep(0)


