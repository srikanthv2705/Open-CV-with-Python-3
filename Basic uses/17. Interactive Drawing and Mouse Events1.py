import cv2
import numpy as np

#Create a black image window
window_Name = "Painting"
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(window_Name)

#Mouse callback function here we are using Left button Double click
def draw_circle(event,x, y, flags, param ):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,0,255),-1)
#Mouse callback function here we are using Middle button Down
    if event == cv2.EVENT_MBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,255,255),-1)

#Mouse callback function here we are using Left button Down
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),30,(0,255,0),-1)


#bind the call back function to window
cv2.setMouseCallback(window_Name, draw_circle)

def main():
    
   while True:
       cv2.imshow(window_Name,img)
       if cv2.waitKey(20) == 27:
           break
       
   cv2.destroyAllWindows() 
       
if __name__ == "__main__":
    main()