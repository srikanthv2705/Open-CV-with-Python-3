import cv2
import numpy as np

def main():
    
    vid_cap = cv2.VideoCapture(0)    
  
    if vid_cap.isOpened():
        ret, frame = vid_cap.read()
        
    else:
        ret = False
        
    while ret:
        ret, frame = vid_cap.read()
        
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        #Blue Color Tracking
        low = np.array([100,50,50])
        high = np.array([140,255,255])
        
        image_mask =cv2.inRange(hsv,low,high)
        output = cv2.bitwise_and(frame,frame,mask = image_mask)
              
        cv2.imshow("Image Mask",image_mask)
        cv2.imshow("Web cam preview", frame)
        cv2.imshow("Color Tracking", output)
        
        if cv2.waitKey(1) == 27: #it exits when we press esc key
            break
    cv2.destroyAllWindows()
    vid_cap.release()
    
if __name__ == "__main__":
    main()
            