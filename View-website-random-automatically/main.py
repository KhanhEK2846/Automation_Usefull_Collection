from selenium import webdriver
import time,random

print("View website random automatically")
links = input("\nLinks (, ): ").split(", ")
n = int(input("Times view: "))
delay = float(input("Delay between view: "))


driver = webdriver.Chrome()

for i in range(n):
    print("\nWeb",i + 1,":")
    driver.get(random.choice(links))
    time.sleep(delay)

driver.quit() 
print("\nDone")




