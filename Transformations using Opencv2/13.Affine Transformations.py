import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    Source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath = Source + "4.2.01.tiff"
    
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img.shape
    
    point1 = np.float32([[100,100],[300,100],[100,300]]) #Affine Transfermations require 3 Noncolliners points
    point2 = np.float32([[250,150],[300,150],[350,300]])
    
    A = cv2.getAffineTransform(point1, point2)
    
    print(A)
    
    output = cv2.warpAffine(img, A, (columns,rows))
    
    plt.imshow(output)
    plt.title("Affine Tranformed image")
    plt.show()
    
if __name__ == '__main__':
    main()