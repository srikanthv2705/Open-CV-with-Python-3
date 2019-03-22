# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:31:28 2019

@author: Srikanth
"""

import cv2
import numpy as np

def main():
    
    img = np.zeros((512,512,3),np.uint8) #Black image
    windowName = "OpenCV BGR Color Pallete"
    cv2.namedWindow(windowName)
    
    while True:
        cv2.imshow(windowName,img)
        
        if cv2.waitKey(0) == 27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()