import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    imgpath = source+ "4.2.03.tiff"
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    box = cv2.boxFilter(img,-1,(38,38))
    
    blur = cv2.blur(img,(17,17))
    
    gaussian = cv2.GaussianBlur(img,(27,27),0)
    
    out = [img,box,blur,gaussian]
    
    title = ['Actual Image','Box filter','Blur','Gaussian Blur']
    
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(out[i])
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
    
    plt.show()
    
if __name__ =='__main__':
    main()