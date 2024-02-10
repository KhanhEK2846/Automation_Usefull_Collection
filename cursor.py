import pyautogui as pg
import random as rd

width, height = pg.size()

while True:
    x= rd.randint(0,width)
    y=rd.randint(0,height)
    pg.moveTo(x,y)