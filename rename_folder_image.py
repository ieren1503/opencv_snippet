# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("./total_images_refinery/")): 
        dst = str(count) + ".jpg"
        src ='./total_images_refinery/'+ filename 
        dst ='./total_images_refinery_rename/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
