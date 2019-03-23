import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    Source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath = Source + "gray.512.tiff"
    
    img = cv2.imread(imgpath,1)
    
    thresh = 127 #exact mid value 
    max_val = 255
    
    ret, out1 = cv2.threshold(img, thresh,max_val,cv2.THRESH_BINARY)
    ret, out2 = cv2.threshold(img, thresh,max_val,cv2.THRESH_BINARY_INV)
    ret, out3 = cv2.threshold(img, thresh,max_val,cv2.THRESH_TOZERO)
    ret, out4= cv2.threshold(img, thresh,max_val,cv2.THRESH_TOZERO_INV)
    ret, out5 = cv2.threshold(img, thresh,max_val,cv2.THRESH_TRUNC)
        
    output = [ img, out1, out2, out3, out4, out5]
    
    titles = ['Actual Image','Binary','Binary_inv','Zero','Zero_inv','Trunc']
    
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()
    
if __name__ == '__main__':
    main()