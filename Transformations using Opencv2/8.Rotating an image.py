import cv2
import matplotlib.pyplot as plt
#import numpy as np

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath1 = source + "4.2.01.tiff"
    
    img = cv2.imread(imgpath1,1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img.shape
    
    R = cv2.getRotationMatrix2D((columns/2,rows/2),45,0.5) # 45 indicates Rotation Degrees ,0.5 is Image size
    
    print(R)
    
    output = cv2.warpAffine(img,R, (columns,rows))
        
    plt.imshow(output)
    plt.title("Rotating an image")
    plt.show()
    
if __name__ == '__main__':
    main()