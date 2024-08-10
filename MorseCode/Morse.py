from MorseTable import MorseTable as mt
import winsound as ws
import time as t
from duration import *

frequency = 2500  # Set Frequency To 2500 Hertz

file = open("input.txt","r")
inData = file.read()
inData = inData.upper()

for character in inData:
    print(character)

    if character == ' ' or character == '\n':
        t.sleep(duration_leter/1000)
        continue
    t.sleep((duration_word-duration_d_d)/1000)

    for x in mt[character]:

        if x == 0:
            ws.Beep(frequency,duration_dot)
        elif x == 1:
            ws.Beep(frequency,duration_dash)
        t.sleep(duration_d_d/1000)

file.close()
