import pyautogui as pg
import pyperclip as pc 

pg.hotkey("win","r")
pc.copy("cmd")
pg.hotkey("ctrl","v")
pg.hotkey("ctrl","shift","enter")