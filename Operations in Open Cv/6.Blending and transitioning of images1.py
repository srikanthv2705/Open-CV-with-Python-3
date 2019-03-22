import cv2
#import matplotlib.pyplot as plt
import numpy as np
import time

def main():
    
    path = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    img_path1 = path + "4.2.01.tiff"
    img_path2 = path + "4.2.03.tiff"
    
    img1 = cv2.imread(img_path1,1)
    img2 = cv2.imread(img_path2,1)
    
#    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
#    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    
    for i in np.linspace(0,1,100):
        alpha = i
        beta = 1-alpha
        output = cv2.addWeighted(img1,alpha,img2,beta,0)
        cv2.imshow("Transition",output)
        time.sleep(0.25)
        if cv2.waitKey(1)==27:
            break
                
    cv2.destroyAllWindows()    
    
if __name__ == "__main__":
    main()
            