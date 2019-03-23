import cv2
import matplotlib.pyplot as plt
#import numpy as np

def main():
    
    source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    imgpath = source+ "5.1.11.tiff"
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    edges = cv2.Laplacian(img,-1,ksize=27,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT) #KSIZE must be odd, shuldnot exceed 31
    output = [img,edges]
    title = ['Actual','Edges']
    
    for i in range(2):
        plt.subplot(1,2,i+1)
        plt.imshow(output[i],cmap='gray')
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
if __name__ =='__main__':
    main()