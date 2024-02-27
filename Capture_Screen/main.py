import pyautogui as pg
import time
from datetime import datetime as dt

def Capture_Screen():
    screenshot = pg.screenshot()
    now = dt.now()
    date_time = now.strftime("%Y%m%d-%H%M%S")
    path = f"screenshots/{date_time}.png"
    screenshot.save(path)
    
while True:
    Capture_Screen()
    time.sleep(1)