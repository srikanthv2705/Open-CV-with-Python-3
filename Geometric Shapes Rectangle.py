import cv2
import numpy as np

def main():
    
    img = np.zeros((512,512,3),np.uint8) # it indicates color image
    
    cv2.line(img,(0,100),(100,0),(255,0,0),2) #last tuple indicates color 1st one is for Blue, last one is for thickness of line
    cv2.rectangle(img,(50,120),(120,80),(0,255,0),2)
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
if __name__ == "__main__":
    main()