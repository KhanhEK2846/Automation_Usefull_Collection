from rembg import remove 
from PIL import Image 
import os,pathlib

dirPath = pathlib.Path(__file__).parent.absolute()
inPath = str(dirPath) + ".\input\\"
outPath = str(dirPath) + ".\output\\"

dirs =os.listdir(inPath)

if __name__ == '__main__':
    for item in dirs:
        img = Image.open(inPath + item)
        img = remove(img)
        img.save(outPath+item)