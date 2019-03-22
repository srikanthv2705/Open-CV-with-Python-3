import cv2
import numpy as np

def main():
    
    img = np.zeros((512,512,3),np.uint8) # it indicates color image
    
    cv2.line(img,(0,100),(100,0),(255,0,0),2) #last tuple indicates color 1st one is for Blue, last one is for thickness of line
    cv2.rectangle(img,(50,120),(120,80),(0,255,0),2)
    cv2.circle(img,(150,150),20,(0,0,255),-1) #-1 fills the total circle
    cv2.ellipse(img, (160,270),(70,30),0,0,360,(248,169,175),-1)
    
    points = np.array([[180,15],[130,60],[190,25],[230,46],[50,90]],np.int32)
    points = points.reshape((-1,1,2))
    cv2.polylines(img, [points],True,(163,198,238))

    text = "SampleText"
    cv2.putText(img, text, (120,210),cv2.FONT_HERSHEY_SIMPLEX,2,(160,235,169))
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
if __name__ == "__main__":
    main() 
