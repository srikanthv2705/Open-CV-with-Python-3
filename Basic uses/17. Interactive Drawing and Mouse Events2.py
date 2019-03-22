import cv2
import numpy as np

#Create a black image window
window_Name = "Painting"
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(window_Name)

#if mouse is pressed it is True
paint = False

#if True, Draw Rectangle. Press 'v' to toggle to curve
mode = True
(ix, iy) =(-1,-1)

#Mouse callback function 
def draw_event(event,x, y, flags, param ):
    global ix, iy, paint, mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        paint = True
        (ix, iy) = x , y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if paint == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
            else:
                cv2.line(img,(ix,iy),(x,y),(0,255,0),2)

    elif event == cv2.EVENT_LBUTTONUP:
        if paint == False:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
            else:
                cv2.line(img,(ix,iy),(x,y),(0,255,0),2)               

#bind the call back function to window
cv2.setMouseCallback(window_Name, draw_event)

def main():
    global mode
    
    while True:
        cv2.imshow(window_Name,img)
        
        k = cv2.waitKey(1)
        if k == ord('v') or k == ord("V"):
            mode = not mode
        elif k == 27:
            break
    cv2.destroyAllWindows()
        
if __name__ == "__main__":
    main()