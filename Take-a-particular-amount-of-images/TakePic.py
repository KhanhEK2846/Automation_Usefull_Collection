import os
import time
import uuid
import cv2 as cv

Image_Path = os.path.join('data','images')
num_images = 30

cap = cv.VideoCapture(0)
for img in range (num_images):
    ret, frame = cap.read()
    Image_Name = os.path.join(Image_Path,f'{str(uuid.uuid1())}.jpg')
    cv.imwrite(Image_Name,frame)
    cv.imshow('Camera',frame)
    time.sleep(0.5)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()