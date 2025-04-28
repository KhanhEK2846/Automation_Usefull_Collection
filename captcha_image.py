from captcha.image import ImageCaptcha
import random, string, pathlib

dirPath = pathlib.Path(__file__).parent.absolute()
outPath = str(dirPath) + ".\output\\"

def geberate_captcha_text(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_captcha_image(text, width=300):
    image = ImageCaptcha(width=width)
    data = image.generate(text)
    image_path = outPath + f"{text}.png"
    image.write(text, image_path)
    return image_path

captcha_text = geberate_captcha_text()
captcha_image_path = generate_captcha_image(captcha_text)
