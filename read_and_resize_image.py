import os
from PIL import Image
import cv2

image_name = 0

for i in range(0,len(os.listdir('C:\\Users\\..'))):
      img=cv2.imread("C:\\Users\\..\\" + str(i)+'.jpg') 
      #We resize the image to dimension 100x100 and store result in var resized_image
      resized_image=cv2.resize(img,(200,200)) 
      #Save the result on disk in the "small" folder
      cv2.imwrite("C:\\Users\\..\\" + str(i)+'.jpg',resized_image)
      print(i)
        
