import os, pathlib, random
from PIL import Image
from glitch_this import ImageGlitcher

# Path
dirPath = pathlib.Path(__file__).parent.absolute()
inPath = str(dirPath) + ".\input\\"
outPath = str(dirPath) + ".\output\\"

dirs =os.listdir(inPath)

# Glitcher
glitcher = ImageGlitcher()

# Seed
random.seed(random.randint(1,99999999999))
seed = random.random()
def Glitch():
    for item in dirs:
        img = Image.open(inPath + item)
        width, height = img.size
        f,e = os.path.splitext(outPath + item)

        imgG = glitcher.glitch_image(img,8,color_offset= True,seed=seed)
        imgG.save(f +'.png')

if __name__ == "__main__":
    Glitch()