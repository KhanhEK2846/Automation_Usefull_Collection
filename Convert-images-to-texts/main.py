from pywhatkit import image_to_ascii_art as tk
import os, pathlib


dirPath = pathlib.Path(__file__).parent.absolute()
inPath = str(dirPath) + ".\input\\"
outPath = str(dirPath) + ".\output\\"

dirs =os.listdir(inPath)

def convert():
    for item in dirs:
        img = inPath + item
        f,e = os.path.splitext(outPath + item)
        tk(img,f)


convert()       