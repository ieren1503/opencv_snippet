import os
from PIL import Image
import cv2

image_name = 0
# ~ print(os.listdir('C:\\Users\\eren\\OneDrive\\Desktop\\colab_results\\bayrak'))
for i in range(0,len(os.listdir('C:\\Users\\eren\\OneDrive\\Desktop\\colab_results\\bayrak'))):
      img=cv2.imread("C:\\Users\\eren\\OneDrive\\Desktop\\colab_results\\bayrak\\" + str(i)+'.jpg') 
      #We resize the image to dimension 100x100 and store result in var resized_image
      resized_image=cv2.resize(img,(200,200)) 
      #Save the result on disk in the "small" folder
      cv2.imwrite("C:\\Users\\eren\\OneDrive\\Desktop\\colab_results\\bayrak_resize\\" + str(i)+'.jpg',resized_image)
      print(i)
        
