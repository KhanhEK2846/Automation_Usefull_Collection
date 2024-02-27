from PIL import Image
import os, pathlib

print("Tool resize & convert images")
w = float(input("\nTimes width resize images: "))
h = float(input("Times height resize images : "))
ic = input("Image converter to: ")
q = int(input("Image quality: "))

dirPath = pathlib.Path(__file__).parent.absolute()
inPath = str(dirPath) + ".\input\\"
outPath = str(dirPath) + ".\output\\"

dirs =os.listdir(inPath)

def resize():
    for item in dirs:
        img = Image.open(inPath + item)
        width, height = img.size
        f,e = os.path.splitext(outPath + item)

        imgR = img.resize((int(width*w), int(height*h)),Image.ANTIALIAS)
        if imgR.mode in ("RGBA","P"):
            imgR = imgR.convert("RGB")
        imgR.save(f +'.'+ ic ,quality = q)

resize()