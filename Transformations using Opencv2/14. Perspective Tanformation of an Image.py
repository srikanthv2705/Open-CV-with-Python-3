import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    Source = "C:\\Users\\Srikanth\\Desktop\\Python\\Opencv\\Dataset\\"
    
    imgpath = Source + "4.2.01.tiff"
    
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img.shape
    
    point1 = np.float32([[0,0],[400,0],[0,400],[400,400]]) #Perspective Transfermations require 4 Noncolliners points
    point2 = np.float32([[0,0],[0,300],[300,0],[300,300]])
    
    P = cv2.getPerspectiveTransform(point1, point2)
    
    print(P)
    
    output = cv2.warpPerspective(img, P, (columns,rows))
    
    plt.imshow(output)
    plt.title("Perspective Tranformed image")
    plt.show()
    
if __name__ == '__main__':
    main()