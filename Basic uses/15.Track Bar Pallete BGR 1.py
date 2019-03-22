import cv2
import numpy as np

def emptyFunction():
    pass

def main():
    
    img = np.zeros((512,512,3),np.uint8) #Black image
    windowName = "OpenCV BGR Color Pallete"
    cv2.namedWindow(windowName)

    cv2.createTrackbar("B", windowName, 0, 255, emptyFunction)
    cv2.createTrackbar("G", windowName, 0, 255, emptyFunction)
    cv2.createTrackbar("R", windowName, 0, 255, emptyFunction)
    
    while True:
        cv2.imshow(windowName, img)
        
        if cv2.waitKey(1) == 27:
            break
    
        Blue = cv2.getTrackbarPos("B",windowName)
        Green = cv2.getTrackbarPos("G",windowName)
        Red = cv2.getTrackbarPos("R",windowName)
    
        img[:] = [Blue,Green,Red]
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()