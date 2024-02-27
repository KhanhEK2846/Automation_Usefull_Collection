import requests
from bs4 import BeautifulSoup
import uuid

print("\n Tool Download All Images in Web")

url = input("\nWebsite: ")
page = requests.get(url)

downloadPath = ".\Img_Down\\"
main_url = url.split('/')[0]+"//"+url.split('/')[2]

soup = BeautifulSoup(page.content,"html.parser")
images = soup.find_all("img")

def CheckName(fileName):
    commons= ['png',"gif","jpeg" , "jpg" , "webp","jpeg","tiff",'psd','pdf','eps','ai','heic','raw','svg']
    for common in commons:
        if common in fileName:
            fileName = fileName = f'{str(uuid.uuid1())}.' + common
            return fileName
    return f'{str(uuid.uuid1())}.jpg'

print("Start downloading...")

for image in images:
    Data = None
    if "data-src" in str(image):
        Data = image["data-src"]
    else:
        Data = image["src"]
    
    if "https:/" not in Data and "http:/" not in Data:
        Data = main_url + Data
    fileName = CheckName(Data)
    
    response = requests.get(Data)
    file = open(downloadPath + fileName, "wb")
    file.write(response.content)
    file.close()
    
print("Done")
