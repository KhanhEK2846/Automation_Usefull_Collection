import cv2, os, pathlib

print("Make outline from images")
ic = input("\nOutline converter to: ")

dirPath = pathlib.Path(__file__).parent.absolute()
inPath = str(dirPath) + ".\input\\"
outPath = str(dirPath) + ".\output\\"

dirs =os.listdir(inPath)

def convert():
    for item in dirs:
        img = cv2.imread(inPath + item)
        f,e = os.path.splitext(outPath + item)
        grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        invert = cv2.bitwise_not(grey_img)
        blur = cv2.GaussianBlur(invert,(21,21),0)
        invertb = cv2.bitwise_not(blur)
        sketch = cv2.divide(grey_img,invertb,scale = 256.0)

        cv2.imwrite(f + "." + ic,sketch)
convert()       